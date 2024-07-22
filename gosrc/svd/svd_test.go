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

	names := make([]string, rows)
	data := make([]float64, rows*cols)
	for i := range data {
		data[i] = rand.NormFloat64()
		if i < rows {
			names[i] = "test"
		}
	}

	reduced := CompressAndVisualize(data, rows, cols, toDim, names)

	assert.NotNil(t, reduced)

}
