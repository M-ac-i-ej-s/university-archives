package main

import (
	"fmt"
)

func main() {
	var i float32

	fmt.Print("Type a number: ")
	fmt.Scan(&i)

	var mars float32 = i / 1.88
	var wenus float32 = i * 365 / 225

	fmt.Println("Na marsie miałbyś " + fmt.Sprintf("%.2f", mars) + "lat")
	fmt.Println("Na wenus miałbyś " + fmt.Sprintf("%.2f", wenus) + " lat")
}
