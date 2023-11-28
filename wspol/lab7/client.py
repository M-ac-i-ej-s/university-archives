import random
import socket
import time

game_map = {0: "rock", 1: "paper", 2: "scissors"}

serverAddressPort = ("127.0.0.1", 1234)
clientAddressPort = ("127.0.0.1", random.randint(1235, 80000))
bufSize = 1024

UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

points = 0
rounds = 0

while True:
    time.sleep(random.random() * 2)

    choice = int(input("type a number: 0 - rock, 1 - paper, 2 - scissors, 3 - end of the game: "))

    if choice == 3:
        print("koniec gry")
        UDPClientSocket.sendto("koniec".encode(), serverAddressPort)
        break

    print(f"I chose {game_map[choice]}")

    UDPClientSocket.sendto(str(choice).encode(), serverAddressPort)
    response, address = UDPClientSocket.recvfrom(bufSize)
    response = response.decode()

    if response == "koniec":
        print("Second player ended game :-(")
        break
    elif response == "draw":
        print("It was draw...")
    elif int(response) == choice:
        print("I won this one")
        points += 1
    else:
        print("Unlucky, I lost...")

    rounds += 1    

print(f"Final score {points}/{rounds}")