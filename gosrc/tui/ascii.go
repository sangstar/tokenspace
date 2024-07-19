package tui

/*
Need to do a number of things:

1. Establish how much whitespace each ║ and ╬ and ═ characters get to
work out how to translate unit vectors correctly in to this space (x and y are normally
of equal distance 1, whereas ║ may be 1.4 * ihat and ═ may be 1.2 * jhat

2. Work out how to translate points on to this graph

3. Work out how to position the graph based on window sizes, and make this plotting
smarter with function closures

4. Work out how we want to denote that the origin unlabeled is the central word


*/

func Plot(windowSize int, data [][]float64) string {
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
