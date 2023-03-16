package main

import "fmt"

func main() {

	slice := make([][]float64, 3)
	for i := range slice {
		slice[i] = make([]float64, 3)
	}

	for i := range slice {
		for k := range slice[i] {
			slice[i][k] = float64(i + k)
		}
	}

	for i := range slice {
		fmt.Println()
		for k := range slice[i] {
			fmt.Print(slice[i][k])
			fmt.Print(" ")
		}
	}
}
