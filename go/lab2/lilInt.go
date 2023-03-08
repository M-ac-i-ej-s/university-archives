package main

import "fmt"

func main() {
	var arrayNum [30]int

	var a, b uint
	b = 1
	n := 30
	for n--; n > 0; n-- {
		a += b
		fmt.Println(a)
		fmt.Println(b)
		arrayNum[n-1]++
		a, b = b, a
	}

	fmt.Println(arrayNum)
}
