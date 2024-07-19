package tui

import (
	"fmt"
	"testing"
)

func TestPlot(t *testing.T) {
	data := [][]float64{
		{1, 2, 3},
		{1, 2, 3},
	}
	fmt.Println(Plot(10, data))
}
