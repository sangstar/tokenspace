package tui

import (
	"bufio"
	"cmp"
	"fmt"
	"log"
	"math"
	"os"
	"os/exec"
	"slices"
	"strings"
)

func readUserInput() string {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter text (exit! to escape): ")
	text, _ := reader.ReadString('\n')
	return strings.Replace(text, "\n", "", -1)
}

func clearScreen() {
	c := exec.Command("clear")
	c.Stdout = os.Stdout
	c.Run()
}

func Plot(xWindowSize, yWindowSize int, closeSet *ClosenessSet) string {
	var xMax float64 = 0
	var yMax float64 = 0

	words := closeSet.CloseWords
	data := make([][]float64, len(words))
	centralVec := closeSet.CentralWord
	for i, d := range words {
		d.Word.Vector2D[0] -= centralVec.Vector2D[0]
		d.Word.Vector2D[1] -= centralVec.Vector2D[1]

		if math.Abs(d.Word.Vector2D[0]) > float64(xMax) {
			xMax = math.Abs(d.Word.Vector2D[0])
		}
		if math.Abs(d.Word.Vector2D[1]) > yMax {
			yMax = math.Abs(d.Word.Vector2D[1])
		}
		data[i] = d.Word.Vector2D
	}

	// Normalize by
	for _, d := range words {
		d.Word.Vector2D[0] = float64(float32(math.Round((d.Word.Vector2D[0] / xMax) * float64(xWindowSize))))
		d.Word.Vector2D[1] = float64(float32(math.Round((d.Word.Vector2D[1] / yMax) * float64(yWindowSize))))
	}

	// Sort points by length in y

	ySorter := func(p1, p2 []float64) int {
		return cmp.Compare(p2[1], p1[1])
	}
	slices.SortFunc(data, ySorter)

	graphic := ""

	for y := yWindowSize; y >= -yWindowSize; y-- {
		line := ""
		for x := -xWindowSize; x <= xWindowSize; x++ {
			if y == 0 && x == 0 {
				line += "\033[31m┼\033[0m"
			}

			for _, word := range words {
				if int(word.Word.Vector2D[0]) == x && int(word.Word.Vector2D[1]) == y {
					line += fmt.Sprintf("(%s)", word.Word.Name)
					// graphic += fmt.Sprintf("¤ %s", word.name)
					//graphic += fmt.Sprintf("¤ %s (%.1f, %.1f)", word.name, word.vector[0], word.vector[1])
				}
			}
			line += " "

		}
		line += "\n"
		graphic += line

	}
	return graphic
}

func visualize(results *ResultSet) error {
	for {
		centralWord := readUserInput()
		clearScreen()
		if centralWord == "exit!" {
			os.Exit(1)
		}
		centralWordToUse, err := results.getWordFromName(centralWord)
		if err != nil {
			log.Printf("Error getting word from name: %v", err)
			continue
		}
		data := getClosenessSet(centralWordToUse, results)
		data.CloseWords = data.CloseWords[:results.svdResult.N]
		res := Plot(results.svdResult.WindowSizeX, results.svdResult.WindowSizeY, data)
		if res == "" {
			return fmt.Errorf("drew nothing")
		}
		fmt.Println(res)
	}

	return nil
}

func Visualize(res *Result) error {
	clearScreen()
	return visualize(processPyData(res))
}
