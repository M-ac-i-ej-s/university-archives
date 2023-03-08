package main

import (
	"fmt"
	"math"
)

func main() {
	var a float64
	var b float64
	var c float64

	fmt.Print("We're gonna calculate this ax^2+bx+c")
	fmt.Print("Set a : ")
	fmt.Scan(&a)
	fmt.Print("Set b : ")
	fmt.Scan(&b)
	fmt.Print("Set c : ")
	fmt.Scan(&c)

	var delta float64 = math.Pow(b, 2) - 4*a*c
	if delta < 0 {
		fmt.Println("nie ma pierwiastków")
		return
	}
	var x1 float64 = (-b - math.Pow(delta, 1/2)) / 2 * a
	var x2 float64 = (-b + math.Pow(delta, 1/2)) / 2 * a

	fmt.Println(x1)
	fmt.Println(x2)
}
