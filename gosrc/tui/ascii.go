package tui

import (
	"cmp"
	"fmt"
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

var windowPadding int = 5

func Plot(words []*Word) string {

	var xMax float32 = 0
	var yMax float32 = 0

	data := make([][]float32, len(words))
	for i, d := range words {
		if d.vector[0] > xMax {
			xMax = d.vector[0]
		}
		if d.vector[1] > yMax {
			yMax = d.vector[1]
		}
		data[i] = d.vector
	}

	// Sort points by length in y

	ySorter := func(p1, p2 []float32) int {
		return cmp.Compare(p2[1], p1[1])
	}
	slices.SortFunc(data, ySorter)

	// Go down line by line. When y lines from origin (yWindow/2), plot it
	yWindowSize := (int(yMax) + 1) + windowPadding
	xWindowSize := (int(xMax) + 1) * windowPadding

	graphic := ""
	addYTick := func(yVal int) string {
		toAdd := ""
		for i := 0; i < xWindowSize; i++ {
			toAdd = toAdd + " "
			if i == (xWindowSize/2-1) && yVal != 0 {
				toAdd = toAdd + "║"
			}
		}
		return graphic + toAdd
	}

	addXAxis := func() string {
		toAdd := ""
		for i := 0; i < xWindowSize; i++ {
			if i == (xWindowSize / 2) {
				toAdd = toAdd + "╬"
			} else {
				toAdd = toAdd + "═"
			}
		}
		return graphic + toAdd
	}

	var doNotPlotTick bool
	for y := yWindowSize / 2; y > (-1 * yWindowSize / 2); y-- {
		doNotPlotTick = false
		if y == 0 {
			graphic = addXAxis()
		}
		for _, d := range data {
			if int(d[1]) == y {
				// Time to plot a point
				for x := -1 * xWindowSize / 2; x < xWindowSize/2; x++ {
					// If at line of x = 0 (y-axis) and no point, draw the axis line now
					if x == 0 && int(d[0]) != 0 {
						graphic = graphic + "║"
						doNotPlotTick = true
					}
					if int(d[0]) == x {
						graphic += "█"
						if x == 0 {
							doNotPlotTick = true
						}

						// Ensures that if the next point is the y-axis that we still plot the tick
						if x+1 == 0 {
							doNotPlotTick = true
							graphic += fmt.Sprintf("║token (%.1f, %.1f)", d[0], d[1])
						} else {
							graphic += fmt.Sprintf(" token (%.1f, %.1f)", d[0], d[1])
						}

					} else {
						graphic += " "
					}
				}
			}
		}
		if !doNotPlotTick {
			graphic = addYTick(y)
		}
		graphic += "\n"

	}
	return graphic
}

func plot(windowSize int, data [][]float64) string {
	var output string

	yPointsUpperQuartile := windowSize / 4
	yPointsLowerQuartile := windowSize / 4
	for i := 0; i < yPointsUpperQuartile; i++ {
		output += "\t" + "║" + "\n"
	}
	output += "<"
	for i := 0; i < 3; i++ {
		output += "═"
	}
	output += "╬"
	for i := 0; i < windowSize; i++ {
		output += "═"
	}
	output += ">\n"
	for i := 0; i < yPointsLowerQuartile; i++ {
		output += "\t" + "║" + "\n"
	}
	output += "\t" + "║" + "         ■ test"
	return output
}
