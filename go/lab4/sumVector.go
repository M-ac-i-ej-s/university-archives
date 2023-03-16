package main

import "fmt"

func main() {
	var arr1 [20]float64
	var arr2 [20]float64

	for i := 0; i < 20; i++ {
		arr1[i] = 2.0
		arr2[i] = 3.0
	}

	var sum [20]float64

	for i := 0; i < 20; i++ {
		sum[i] = arr1[i] + arr2[i]
	}

	fmt.Println(sum)
}
