package svd

import (
	"github.com/stretchr/testify/assert"
	"math/rand"
	"testing"
)

func TestSVDOnLargeMatrix(t *testing.T) {
	// Define the dimensions of the large matrix
	rows := 50000
	cols := 500

	stackedList := make([][]float64, rows)
	for i := range stackedList {
		stackedList[i] = make([]float64, cols)
		for j := range stackedList[i] {
			stackedList[i][j] = rand.Float64()
		}
	}

	reduced, err := Compress(stackedList, 2)

	assert.Nil(t, err)
	assert.NotNil(t, reduced)

	rowsReduced, colsReduced := reduced.Dims()
	assert.Equal(t, rowsReduced, rows)
	assert.NotEqual(t, colsReduced, cols)
	assert.Equal(t, colsReduced, 2)
}

func TestConversionToDense(t *testing.T) {
	stackedList := make([][]float64, 3)
	for i := range stackedList {
		stackedList[i] = make([]float64, 5)
		for j := range stackedList[i] {
			stackedList[i][j] = rand.Float64()
		}
	}

	converted := ToDense(stackedList)
	convertedRows, convertedCols := converted.Dims()
	assert.Equal(t, convertedRows, 3)
	assert.Equal(t, convertedCols, 5)

}
