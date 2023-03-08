package main

import (
	"fmt"
	"strconv"
)

func main() {
	var i int

	fmt.Print("Type a number: ")
	fmt.Scan(&i)
	fmt.Println("Masz za sobą " + strconv.Itoa(i*12) + " miesięcy")
	fmt.Println("Masz za sobą " + strconv.Itoa(i*365) + " dni")
}
