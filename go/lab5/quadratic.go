package main

import (
	"fmt"
	"math"
)

func main() {
	var a, b, c, d float64
	p("type a b c: ")
	fmt.Scanln(&a, &b, &c)
	d = b*b - 4*a*c
	if d > 0 {
		p("x1 =", (-b+math.Sqrt(d))/2*a, "x2 =", (-b-math.Sqrt(d))/2*a)
	} else {
		if d == 0 {
			p("x=", -b/2*a)
		} else {
			p("brak")
		}
	}
}

func p(t ...interface{}) {
	fmt.Println(t...)
}
