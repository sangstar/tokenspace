package svd

import (
	"fmt"
	"gonum.org/v1/gonum/mat"
	"math"
	"sort"
	"sync"
)

type Word struct {
	name     string
	dim      int
	vector   []float64
	vector2D []float64
	idx      int
}

type CloseWord struct {
	word         *Word
	rankBefore   int
	rankAfter    int
	cosSimBefore float64
	cosSimAfter  float64
	score        float64
}

type ResultSet struct {
	words     *[]*Word
	outputDim int
	svdResult *SVDResult
}

type ClosenessSet struct {
	centralWord *Word
	closeWords  []*CloseWord
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

type SVDResult struct {
	FlattenedCompressed *Vectors
	OriginalData        *Vectors
	Names               *[]string
	OutputDim           int
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

func CompressAndVisualize(List []float64, r int, c int, outputDim int, Names []string) error {
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
	return Visualize(&SVDResult{
		DenseToVectors(&reducedPositions),
		&Vectors{
			Data: &List,
			Rows: rows,
			Cols: c,
		},
		&Names,
		outputDim,
	})

}

func processPyData(svd *SVDResult) *ResultSet {
	numWords := len(*svd.Names)

	names := *svd.Names
	svdVecs := *svd.FlattenedCompressed.Data
	originalVecs := *svd.OriginalData.Data

	reshapedWordVecs := make([]*Word, numWords)
	for i := 0; i < numWords; i++ {
		reshapedWordVecs[i] = &Word{
			name:     names[i],
			vector:   originalVecs[i : i+svd.OriginalData.Cols],
			vector2D: svdVecs[i : i+svd.FlattenedCompressed.Cols],
			idx:      i,
		}
	}

	return &ResultSet{
		words:     &reshapedWordVecs,
		outputDim: numWords,
		svdResult: svd,
	}
}

func Plot(results *ResultSet) string {
	return "not implemented"
}

func visualize(results *ResultSet) error {
	words := *results.words
	getClosenessSet(words[0], results)
	res := Plot(results)
	if res == "" {
		return fmt.Errorf("Drew nothing")
	}
	fmt.Println(res)
	return nil
}

func Visualize(svd *SVDResult) error {
	return visualize(processPyData(svd))
}

func splitVectorizedOp(numWorkers int, jobParams *VecOpParams, by func(*sync.WaitGroup, []*Word, *VecOpParams)) []*CloseWord {
	numVectors := len(*jobParams.results.svdResult.Names)
	remainderVecs := numVectors % numWorkers

	dataToSplit := jobParams.words
	splitAmount := numVectors / numWorkers

	jobParams.wordChan = make(chan []*CloseWord, numWorkers+1)

	wg := &sync.WaitGroup{}
	for i := 0; i < numWorkers; i++ {
		wg.Add(1)
		splicedVecs := dataToSplit[i*splitAmount : (i*splitAmount)+splitAmount]
		go by(wg, splicedVecs, jobParams)
	}

	// Finally, do the remainder vecs
	wg.Add(1)
	splicedVecs := dataToSplit[-remainderVecs:]
	go by(wg, splicedVecs, jobParams)

	wg.Wait()
	close(jobParams.wordChan)

	resultData := make([]*CloseWord, numVectors)
	for result := range jobParams.wordChan {
		for i, data := range result {
			resultData[i] = data
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
		return (float64(numVecs-close.rankAfter) / float64(numVecs)) * 1 / (math.Abs(float64(close.rankBefore-close.rankAfter)) + 1)
	}

	for i, closeWord := range resultData {
		closeWord.rankAfter = i
		closeWord.score = getScore(closeWord)
	}

	sort.Slice(resultData, func(i, j int) bool {
		return resultData[i].score > resultData[j].score
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

	// TODO: Make score include the ranking equation from before,
	//       not just cos sim, where it penalizes rank
	//       differences before and after compression, and a bad rank

	closeWords := make([]*CloseWord, len(words))
	for i := 0; i < len(words); i++ {
		cosSimBefore := cosSim(jobParams.centralWord.vector, words[i].vector)
		cosSimAfter := cosSim(jobParams.centralWord.vector2D, words[i].vector2D)
		closeWords[i] = &CloseWord{
			word:         words[i],
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
		wordChan:    nil,
	}

	numWorkers := 10

	splitVectorizedOp(numWorkers, JobParams, getAdjustedSimilarities)

	return &ClosenessSet{}
}
