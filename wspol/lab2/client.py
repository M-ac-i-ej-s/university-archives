import time
import random
import os

is_lock = True

message = input("Message: ")

fileId = random.randint(1, 123456789)
filePath = str(os.getcwd() + f"/message-{fileId}.txt")

with open(filePath, "w") as file:
    file.close()

while True:
    if not os.path.exists("lockfile"):
        lock = os.open("lockfile", os.O_CREAT | os.O_EXCL | os.O_RDWR)
        print("lockfile created")
        break
    else:
        if is_lock:
            print("Server is in use, plesae wait...")
            is_lock = not is_lock
        time.sleep(1)

with open("buffer.txt", "w") as file:
    file.write(filePath)
    file.write("\n")
    file.write(message)

for x in range(5, -1, -1):
    time.sleep(1)
print("response generated")

with open(filePath, "r") as file:
    print(file.read())

if os.path.exists(filePath):
    os.remove(filePath)
    print(f"file {fileId} is now deleted")
else:
    print("The file does not exist")

os.close(lock)
os.unlink("lockfile")