package main

import (
	"fmt"
	"math/big"
	"strconv"
	"strings"
)

func main() {
	nick := "MacSlu"
	byteArray := []byte(nick)
	n := 1
	x := new(big.Int)
	fmt.Println(byteArray)
	for finished := false; !finished; {
		num := 0
		str := x.MulRange(1, int64(n)).String()
		for i := 0; i < len(byteArray); i++ {
			if strings.Contains(str, strconv.Itoa(int(byteArray[i]))) {
				num++
			}
		}
		if num == len(byteArray) {
			finished = true
		} else {
			n++
		}
	}
	fmt.Println(n)

	fmt.Println(x.MulRange(1, int64(n)))
}

// fibonacci recursion function

func fib(n int) int {
	if n <= 1 {
		return n
	}
	fmt.Print(n)
	return fib(n-1) + fib(n-2)
}
