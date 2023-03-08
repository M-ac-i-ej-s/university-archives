package main

import (
	"fmt"
	"math/rand"
	"strconv"
)

func main() {
	var randomInt int = rand.Intn(100)
	var guess int

	fmt.Println("Lets play!")
	fmt.Println("aby zakończyć napisz 'koniec'")

	for guess != randomInt {
		fmt.Print("guess a number between 1 and 100: ")
		fmt.Scan(&guess)
		if message == "koniec" {
			fmt.Println("Żegnaj")
			return
		} else if guess < randomInt {
			fmt.Println("try a higher number")
		} else if guess > randomInt {
			fmt.Println("try a lower number")
		}
	}

	fmt.Print("You made it! the number is " + strconv.Itoa(guess))
}
