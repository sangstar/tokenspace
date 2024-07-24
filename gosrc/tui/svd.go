package tui

import (
	"fmt"
	"gonum.org/v1/gonum/mat"
	"math"
	"sort"
	"sync"
)

type Word struct {
	Name     string
	Dim      int
	Vector   []float64
	Vector2D []float64
	Idx      int
}

type CloseWord struct {
	Word         *Word
	rankBefore   int
	rankAfter    int
	cosSimBefore float64
	cosSimAfter  float64
	Score        float64
}

type ResultSet struct {
	words     *[]*Word
	outputDim int
	svdResult *Result
}

type ClosenessSet struct {
	CentralWord *Word
	CloseWords  []*CloseWord
}

type Vectors struct {
	Data *[]float64
	Rows int
	Cols int
}

type VecOpParams struct {
	centralWord *Word
	words       []*Word
	results     *ResultSet
	wordChan    chan []*CloseWord
}

type Result struct {
	FlattenedCompressed *Vectors
	OriginalData        *Vectors
	Names               *[]string
	OutputDim           int
	N                   int
	WindowSizeX         int
	WindowSizeY         int
	Alpha               float64
	NumWorkers          int
}

func (rs *ResultSet) getWordFromName(name string) (*Word, error) {
	for _, w := range *rs.words {
		if w.Name == name {
			return w, nil
		}
	}
	return nil, fmt.Errorf("could not find word %s", name)
}

func DenseToVectors(m *mat.Dense) *Vectors {
	r, c := m.Dims()
	outputArr := make([]float64, r*c)
	for i := 0; i < r; i++ {
		for j := 0; j < c; j++ {
			outputArr[i*c+j] = m.At(i, j)
		}
	}
	return &Vectors{
		Data: &outputArr,
		Rows: r,
		Cols: c,
	}
}

func CompressAndVisualize(N, WindowSizeX, WindowSizeY, NumWorkers int, Alpha float64, List []float64, r int, c int, outputDim int, Names []string) error {
	m := mat.NewDense(r, c, List)
	var svd mat.SVD
	ok := svd.Factorize(m, mat.SVDThinU)
	rows, _ := m.Dims()
	if !ok {
		panic("factorization failed")
	}
	var U mat.Dense
	svd.UTo(&U)

	sigma := svd.Values(nil)
	U2 := U.Slice(0, rows, 0, outputDim).(*mat.Dense)
	Sigma2 := mat.NewDiagDense(outputDim, sigma[:outputDim])

	// Calculate the reduced positions matrix
	var reducedPositions mat.Dense
	reducedPositions.Mul(U2, Sigma2)
	return Visualize(&Result{
		DenseToVectors(&reducedPositions),
		&Vectors{
			Data: &List,
			Rows: rows,
			Cols: c,
		},
		&Names,
		outputDim,
		N,
		WindowSizeX,
		WindowSizeY,
		Alpha,
		NumWorkers,
	})

}

func processPyData(svd *Result) *ResultSet {
	numWords := len(*svd.Names)

	names := *svd.Names
	svdVecs := *svd.FlattenedCompressed.Data
	originalVecs := *svd.OriginalData.Data

	reshapedWordVecs := make([]*Word, numWords)
	for i := 0; i < numWords; i++ {
		reshapedWordVecs[i] = &Word{
			Name:     names[i],
			Vector:   originalVecs[i*svd.OriginalData.Cols : (i+1)*svd.OriginalData.Cols],
			Vector2D: svdVecs[i*svd.FlattenedCompressed.Cols : (i+1)*svd.FlattenedCompressed.Cols],
			Idx:      i,
		}
	}

	return &ResultSet{
		words:     &reshapedWordVecs,
		outputDim: numWords,
		svdResult: svd,
	}
}

func splitVectorizedOp(jobParams *VecOpParams, by func(*sync.WaitGroup, []*Word, *VecOpParams)) []*CloseWord {
	numVectors := len(*jobParams.results.svdResult.Names)
	numWorkers := jobParams.results.svdResult.NumWorkers
	alpha := jobParams.results.svdResult.Alpha
	remainderVecs := numVectors % numWorkers

	dataToSplit := jobParams.words
	splitAmount := numVectors / numWorkers

	wg := &sync.WaitGroup{}
	for i := 0; i < numWorkers; i++ {
		wg.Add(1)
		splicedVecs := dataToSplit[i*splitAmount : (i*splitAmount)+splitAmount]
		go by(wg, splicedVecs, jobParams)
	}

	// Finally, do the remainder vecs
	wg.Add(1)
	splicedVecs := dataToSplit[len(dataToSplit)-remainderVecs:]
	go by(wg, splicedVecs, jobParams)

	wg.Wait()
	close(jobParams.wordChan)

	i := 0
	resultData := make([]*CloseWord, numVectors)
	for result := range jobParams.wordChan {
		for _, data := range result {
			resultData[i] = data
			i++
		}
	}

	sort.Slice(resultData, func(i, j int) bool {
		return resultData[i].cosSimBefore > resultData[j].cosSimBefore
	})

	for i, closeWord := range resultData {
		closeWord.rankBefore = i
	}

	sort.Slice(resultData, func(i, j int) bool {
		return resultData[i].cosSimAfter > resultData[j].cosSimAfter
	})

	numVecs := len(resultData)
	getScore := func(close *CloseWord) float64 {
		beforePerformance := float64(numVecs-close.rankBefore) / float64(numVecs)
		//afterPerformance := float64(close.rankAfter / numVecs)
		rankDrift := (float64(numVecs) - math.Abs(float64(close.rankBefore-close.rankAfter))) / float64(numVecs)
		return beforePerformance + (alpha * rankDrift)
	}

	for i, closeWord := range resultData {
		closeWord.rankAfter = i
		closeWord.Score = getScore(closeWord)
	}

	sort.Slice(resultData, func(i, j int) bool {
		return resultData[i].Score > resultData[j].Score
	})

	return resultData

}

func getAdjustedSimilarities(wg *sync.WaitGroup, words []*Word, jobParams *VecOpParams) {
	defer wg.Done()

	cosSim := func(a, b []float64) float64 {
		vecA := mat.NewVecDense(len(a), a)
		vecB := mat.NewVecDense(len(b), b)
		return mat.Dot(vecA, vecB) / (vecA.Norm(2) * vecB.Norm(2))
	}

	closeWords := make([]*CloseWord, len(words))
	for i := 0; i < len(words); i++ {
		cosSimBefore := cosSim(jobParams.centralWord.Vector, words[i].Vector)
		cosSimAfter := cosSim(jobParams.centralWord.Vector2D, words[i].Vector2D)
		closeWords[i] = &CloseWord{
			Word:         words[i],
			cosSimBefore: cosSimBefore,
			cosSimAfter:  cosSimAfter,
		}
	}

	jobParams.wordChan <- closeWords

	return
}

func getClosenessSet(centralWord *Word, results *ResultSet) *ClosenessSet {

	JobParams := &VecOpParams{
		centralWord: centralWord,
		words:       *results.words,
		results:     results,
		wordChan:    make(chan []*CloseWord, len(*results.words)),
	}

	closeWords := splitVectorizedOp(JobParams, getAdjustedSimilarities)

	return &ClosenessSet{
		CentralWord: centralWord,
		CloseWords:  closeWords[1:], // disregard first index as that will be central word
	}
}
