package main

import (
	"fmt"
	"sort"
)

func main() {

	slice := make([][]float64, 10)
	slice2 := make([][]float64, 10)
	for i := range slice {
		slice[i] = make([]float64, 10)
		slice2[i] = make([]float64, 10)
	}

	for i := range slice {
		for k := range slice[i] {
			slice[i][k] = float64((i + 1) * (k + 1))
			slice2[9-i][k] = float64((i + 1) * (k + 1))
		}
		ReverseSlice(slice2[9-i])
	}

	for i := range slice {
		fmt.Println()
		for k := range slice[i] {
			fmt.Print(slice[i][k])
			fmt.Print(" ")
		}
	}

	fmt.Print(" ")

	for i := range slice2 {
		fmt.Println()
		for k := range slice2[i] {
			fmt.Print(slice2[i][k])
			fmt.Print(" ")
		}
	}

	slice3 := make([][]float64, 10)
	for i := range slice3 {
		slice3[i] = make([]float64, 10)
	}

	for i := range slice3 {
		for k := range slice3[i] {
			slice3[i][k] = float64(slice2[i][k] + slice[i][k])
		}
	}

	for i := range slice3 {
		fmt.Println()
		for k := range slice3[i] {
			fmt.Print(slice3[i][k])
			fmt.Print(" ")
		}
	}
}

func ReverseSlice[T comparable](s []T) {
	sort.SliceStable(s, func(i, j int) bool {
		return i > j
	})
}
