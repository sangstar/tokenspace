package tui

import (
	"cmp"
	"math"
	"slices"
)

/*
Need to do a number of things:

1. Establish how much whitespace each ║ and ╬ and ═ characters get to
work out how to translate unit vectors correctly in to this space (x and y are normally
of equal distance 1, whereas ║ may be 1.4 * ihat and ═ may be 1.2 * jhat

2. Work out how to translate points on to this graph

3. Work out how to position the graph based on window sizes, and make this plotting
smarter with function closures

4. Work out how we want to denote that the origin unlabeled is the central word

5. Need to make sure it fits any screen's terminal size

Probably will need to render one line at a time as it is constructed up to down.
For example, can't already make the y axis but have a point be at (1, 2)
Can maybe just have \n decrement in y and " " increment in x, decrement by left of ╬

Would be cool if TUI had this graph, and some other stuff like

- a text field to input a new word and generate close points (could also just click on a close point word
and generate for that)
- a list of the coordinates for the close points


*/

func Plot(set *ResultSet) string {
	words := set.SimilarWords
	var xMax float32 = 0
	var yMax float32 = 0

	data := make([][]float32, len(words))
	for i, d := range words {
		d.vector[0] -= set.WordOfInterest.vector[0]
		d.vector[1] -= set.WordOfInterest.vector[1]
		if math.Abs(float64(d.vector[0])) > float64(xMax) {
			xMax = float32(math.Abs(float64(d.vector[0])))
		}
		if math.Abs(float64(d.vector[1])) > float64(yMax) {
			yMax = float32(math.Abs(float64(d.vector[1])))
		}
		data[i] = d.vector
	}

	// Go down line by line
	xWindowSize := 30
	yWindowSize := 10

	// Normalize by
	for _, d := range words {
		d.vector[0] = float32(math.Round(float64((d.vector[0] / xMax) * float32(xWindowSize))))
		d.vector[1] = float32(math.Round(float64((d.vector[1] / yMax) * float32(yWindowSize))))
	}

	// Sort points by length in y

	ySorter := func(p1, p2 []float32) int {
		return cmp.Compare(p2[1], p1[1])
	}
	slices.SortFunc(data, ySorter)

	graphic := ""

	for y := yWindowSize; y >= -yWindowSize; y-- {
		line := ""
		for x := -xWindowSize; x <= xWindowSize; x++ {
			if y == 0 && x == 0 {
				line += "┼"
			}
			for _, word := range words {
				if int(word.vector[0]) == x && int(word.vector[1]) == y {
					line += "|" + word.name + "|"
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
