package svd

import (
	"gonum.org/v1/gonum/mat"
)

func Compress(List []float64, r int, c int, outputDim int) []float64 {
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
	return DenseToArray(&reducedPositions)
}

func DenseToArray(m *mat.Dense) []float64 {
	r, c := m.Dims()
	outputArr := make([]float64, r*c)
	for i := 0; i < r; i++ {
		for j := 0; j < c; j++ {
			outputArr[i*c+j] = m.At(i, j)
		}
	}
	return outputArr
}
