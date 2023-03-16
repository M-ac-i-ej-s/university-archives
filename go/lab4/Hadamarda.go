package main

import "fmt"

func main() {

	var arr1 = [2][3]float64{
		{1, 2, 3},
		{4, 5, 6},
	}

	var arr2 = [2][3]float64{
		{1, 2, 3},
		{4, 5, 6},
	}

	var productArr [2][3]float64

	for i := 0; i < len(arr1); i++ {
		for k := 0; k < len(arr1[0]); k++ {
			productArr[i][k] = arr1[i][k] * arr2[i][k]
		}
	}

	fmt.Println(productArr)
}
