import time
i = int(input("Number: "))

with open("input.txt", "w") as file:
    file.write(str(i))

time.sleep(2)

with open("output.txt", "r") as file:
    print(f"Result: {file.readline()}")

with open("output.txt", "w"):
    pass