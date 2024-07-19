package tui

import "fmt"

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

func ProvePassable(centralWord string, centralWordVec []float32, closestWords []string, closestWordDistances []float32, closestWordVectors []float32) *ResultSet {
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
	fmt.Print(closestWordDistances)
	return &ResultSet{
		WordOfInterest: &Word{name: centralWord, vector: centralWordVec},
		VectorDim:      vectorLength,
		SimilarWords:   reshapedWordVecs,
		Distances:      closestWordDistances,
	}
}
