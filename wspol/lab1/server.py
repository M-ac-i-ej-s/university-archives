import time

print("server is on")

while True:
    l = "a"
    with open("input.txt", "r") as file:
        l = file.readline()
        if len(l) > 0:
            l = int(l)

    if type(l) == int:
        with open("output.txt", "w") as file:
            file.write(f"{l**2}")

        with open("input.txt", "w"):
            pass

    time.sleep(0.5)