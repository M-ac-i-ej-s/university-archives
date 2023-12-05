import random
import socket
import time

game_map = {0: "kamień", 1: "papier", 2: "nożyce"}

serverAddressPort = ("127.0.0.1", 1234)
clientAddressPort = ("127.0.0.1", random.randint(1235, 80000))
bufSize = 1024

UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

points = 0
rounds = 0

while True:
    time.sleep(random.random() * 2)

    choice = int(input("Wybierz cyferkę: 0 - kamień, 1 - papier, 2 - nożyce, 3 - zakończ grę: "))

    if choice == 3:
        print("koniec gry")
        UDPClientSocket.sendto("koniec".encode(), serverAddressPort)
        break

    print(f"wybieram {game_map[choice]}")

    UDPClientSocket.sendto(str(choice).encode(), serverAddressPort)
    response, address = UDPClientSocket.recvfrom(bufSize)
    response = response.decode()

    if response == "koniec":
        print("wpsółgracz zakończył grę")
        break
    elif response == "draw":
        print("remis !")
    elif int(response) == choice:
        print("wygrałeś tę rundę :) !")
        points += 1
    else:
        print("przegraęś tę rundę :( !")

    rounds += 1    

print(f"wygrałeś {points}/{rounds} rund")