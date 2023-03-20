package main

import "fmt"

func main() {

	slice := createSlice(3, 2)

	slice2 := createSlice(2, 3)

	slice3 := createSlice(len(slice), len(slice2[0]))

	for i := range slice {
		for k := range slice[i] {
			slice[i][k] = float64((i + 1) * (k + 1))
		}
	}

	for i := range slice2 {
		for k := range slice2[i] {
			slice2[i][k] = float64((i + 1) * (k + 1))
		}
	}

	for i := range slice3 {
		for k := range slice3 {
			for l := range slice2 {
				slice3[i][k] += slice[i][l] * slice2[l][k]
			}
		}
	}

	printSlice(slice)
	printSlice(slice2)
	printSlice(slice3)
}

func createSlice(x int, y int) [][]float64 {
	slice := make([][]float64, y)

	for i := range slice {
		slice[i] = make([]float64, x)
	}

	return slice
}

func printSlice(slice [][]float64) {
	for i := range slice {
		fmt.Println()
		for k := range slice[i] {
			fmt.Print(slice[i][k])
			fmt.Print(" ")
		}
	}
	fmt.Println()
}
