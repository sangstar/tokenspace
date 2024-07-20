package tui

import "testing"

var centralWord string
var centralWordVec []float32
var similarWords []string
var similarWordDistances []float32
var flattenedClosestWordVectors []float32

func init() {
	centralWord = "hello"
	centralWordVec = []float32{-2.326746940612793, 0.10097233951091766}
	similarWords = []string{"thanks", "thank", "birthday", "welcome", "happy", "hey", "miss", "love", "dear", "babe", "baby", "yes", "pic", "friend", "lovely", "aw", "morning", "sweet", "please", "princess"}
	similarWordDistances = []float32{0.9292945861816406, 0.9241276383399963, 0.921881377696991, 0.9198573231697083, 0.9158350229263306, 0.9121533632278442, 0.9077523350715637, 0.9076114296913147, 0.8950147032737732, 0.8825744390487671, 0.8803675770759583, 0.8730589151382446, 0.867878258228302, 0.8667399287223816, 0.8660722970962524, 0.8643124103546143, 0.8626499176025391, 0.8609232902526855, 0.8605848550796509, 0.8576496243476868}
	flattenedClosestWordVectors = []float32{-2.6002085208892822, -0.09590407460927963, -2.554792881011963, -0.45508235692977905, -2.5613934993743896, 0.14836767315864563, -2.2297744750976562, 0.29182493686676025, -3.2166919708251953, -0.019407732412219048, -2.6950583457946777, 0.4743480384349823, -2.6736180782318115, 0.15542887151241302, -3.2601001262664795, -0.05380437523126602, -1.92204749584198, -0.36105504631996155, -2.0705618858337402, -0.06764644384384155, -2.701164960861206, 0.3952599763870239, -2.771214485168457, -0.26023831963539124, -2.325035572052002, 0.21269506216049194, -2.2219741344451904, -0.4241662919521332, -1.8694411516189575, -0.038843996822834015, -2.5554938316345215, -0.1266227811574936, -2.4951913356781006, 0.5956910252571106, -2.3523411750793457, -0.09082696586847305, -2.899852991104126, -0.4352123439311981, -1.5957920551300049, -0.19177187979221344}
}
func TestVisualize(t *testing.T) {
	Visualize(centralWord, centralWordVec, similarWords, similarWordDistances, flattenedClosestWordVectors)
}