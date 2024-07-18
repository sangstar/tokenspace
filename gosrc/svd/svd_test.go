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

	toDim := 2

	data := make([]float64, rows*cols)
	for i := range data {
		data[i] = rand.NormFloat64()
	}

	reduced := Compress(data, rows, cols, toDim)

	assert.NotNil(t, reduced)
	assert.Equal(t, len(reduced), rows*toDim)

}
