package tui

import (
	"fmt"
)

type Word struct {
	name   string
	dim    int
	vector []float32
}

type ResultSet struct {
	WordOfInterest *Word
	VectorDim      int
	SimilarWords   []*Word
	Distances      []float32
}

func processPyData(centralWord string, centralWordVec []float32, closestWords []string, closestWordDistances []float32, closestWordVectors []float32) *ResultSet {
	/*	// Ensuring Go runtime persists while workers finish task
		wg := sync.WaitGroup{}
		run := func(idx int) {
			defer wg.Done()
			fmt.Println("Simulating work: ", idx)
			time.Sleep(10 * time.Second)
			fmt.Println("Worker ", idx, "complete")
		}
		for i := 0; i < 10; i++ {
			wg.Add(1)
			go run(i)
		}
		wg.Wait()*/

	vectorLength := len(centralWordVec)
	numSimilarTokens := len(closestWords)

	reshapedWordVecs := make([]*Word, numSimilarTokens)
	for i := 0; i < numSimilarTokens; i++ {
		wordAccumulator := make([]float32, vectorLength)
		for j := 0; j < vectorLength; j++ {
			wordAccumulator[j] = closestWordVectors[i+j]
		}
		reshapedWordVecs[i] = &Word{name: closestWords[i], vector: wordAccumulator}
	}

	return &ResultSet{
		WordOfInterest: &Word{name: centralWord, vector: centralWordVec},
		VectorDim:      vectorLength,
		SimilarWords:   reshapedWordVecs,
		Distances:      closestWordDistances,
	}
}

func visualize(results *ResultSet) error {
	return fmt.Errorf("Not yet implemented")
}

func Visualize(centralWord string, centralWordVec []float32, closestWords []string, closestWordDistances []float32, closestWordVectors []float32) error {
	return visualize(processPyData(centralWord, centralWordVec, closestWords, closestWordDistances, closestWordVectors))
}
