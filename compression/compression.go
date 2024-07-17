package compression

import (
	"gonum.org/v1/gonum/mat"
)

func CompressSVD(stackedList [][]float64, outputDim int) (mat.Dense, error) {
	m := ToDense(stackedList)
	var svd mat.SVD
	ok := svd.Factorize(m, mat.SVDThinU)
	rows, _ := m.Dims()
	if !ok {
		return mat.Dense{}, nil
	}
	var U mat.Dense
	svd.UTo(&U)

	sigma := svd.Values(nil)
	U2 := U.Slice(0, rows, 0, outputDim).(*mat.Dense)
	Sigma2 := mat.NewDiagDense(outputDim, sigma[:outputDim])

	// Calculate the reduced positions matrix
	var reducedPositions mat.Dense
	reducedPositions.Mul(U2, Sigma2)
	return reducedPositions, nil
}

func ToDense(stackedList [][]float64) *mat.Dense {
	numRows := len(stackedList)
	numCols := len(stackedList[0])

	contiguousData := make([]float64, numCols*numRows)
	for i := 0; i < numRows; i++ {
		for j := 0; j < numCols; j++ {
			contiguousData[i*numCols+j] = stackedList[i][j]
		}
	}

	return mat.NewDense(numRows, numCols, contiguousData)
}
