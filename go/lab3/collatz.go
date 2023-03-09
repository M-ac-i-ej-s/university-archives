package main

import (
	"fmt"

	"github.com/sbinet/go-gnuplot"
)

func main() {
	var arr []float64
	for i := 0; i < 100000; i++ {
		l := 0
		n := i + 1
		for n != 1 {
			l++
			if n%2 == 0 {
				n = n / 2
			} else {
				n = 3*n + 1
			}
		}
		arr[i] = float64(l)
	}

	fname := ""
	persist := false
	debug := true

	p, err := gnuplot.NewPlotter(fname, persist, debug)
	if err != nil {
		err_string := fmt.Sprintf("** err: %v\n", err)
		panic(err_string)
	}
	defer p.Close()

	var arrNum []float64
	for i := 1.0; i <= 100000; i++ {
		arrNum[int(i)-1] = i
	}

	p.PlotXY(arr, arrNum, "numbers of repetition")
	p.CheckedCmd("set terminal pdf")
	p.CheckedCmd("set output 'plot002.pdf'")
	p.CheckedCmd("replot")

	p.CheckedCmd("q")

	// max, index := findMax(arr)
	// fmt.Println(max, index)
}

func findMax(a [1000]int) (max int, maxIndex int) {
	max = a[0]
	maxIndex = 0
	for index, value := range a {
		if value > max {
			max = value
			maxIndex = index
		}
	}
	return max, maxIndex + 3000
}

// 1) najdłuższy ciąg Collatza jest dla 98 i wynosi 118

// 2)
//  w przedziale 1000-2000 najdłuższy ciąg Collatza jest dla 1161 i wynosi 181
//  w przedziale 2000-3000 najdłuższy ciąg Collatza jest dla 2919 i wynosi 216
//  w przedziale 3000-4000 najdłuższy ciąg Collatza jest dla 3711 i wynosi 237
//  jedyne co łączy te liczby to posiadanie w sobie 1

// 1 to 100000 float array
