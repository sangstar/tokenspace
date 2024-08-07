package tui

import (
	"encoding/json"
	"github.com/stretchr/testify/assert"
	"io/ioutil"
	"os"
	"testing"
)

type TestData struct {
	FlatList []float64 `json:"flat_list"`
	Rows     int       `json:"rows"`
	Cols     int       `json:"cols"`
	Names    []string  `json:"names"`
}

func TestSVDOnLargeMatrix(t *testing.T) {
	file, err := os.Open("../../data.json")
	if err != nil {
		t.Fatalf("Failed to open data.json: %v", err)
	}
	defer file.Close()

	byteValue, err := ioutil.ReadAll(file)
	if err != nil {
		t.Fatalf("Failed to read data.json: %v", err)
	}

	var testData TestData
	err = json.Unmarshal(byteValue, &testData)
	if err != nil {
		t.Fatalf("Failed to unmarshal data.json: %v", err)
	}

	reduced := CompressAndVisualize(20, 10, 10, 10, 0.05, testData.FlatList, testData.Rows, testData.Cols, 2, testData.Names)

	assert.NotNil(t, reduced)

}
