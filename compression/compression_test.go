package compression

import (
	"github.com/stretchr/testify/assert"
	"gonum.org/v1/gonum/mat"
	"math/rand"
	"testing"
	"time"
)

func TestSVDOnLargeMatrix(t *testing.T) {
	// Define the dimensions of the large matrix
	rows := 50000
	cols := 500

	// Seed the random number generator for reproducibility
	rand.Seed(time.Now().UnixNano())

	// Create a slice to hold the random values
	data := make([]float64, rows*cols)

	// Populate the slice with random values
	for i := range data {
		data[i] = rand.Float64()
	}

	// Create a new dense matrix with the random values
	largeMatrix := mat.NewDense(rows, cols, data)

	reduced, err := CompressSVD(largeMatrix, 2)

	assert.Nil(t, err)
	assert.NotNil(t, reduced)

	rowsReduced, colsReduced := reduced.Dims()
	assert.Equal(t, rowsReduced, rows)
	assert.NotEqual(t, colsReduced, cols)
	assert.Equal(t, colsReduced, 2)
}
