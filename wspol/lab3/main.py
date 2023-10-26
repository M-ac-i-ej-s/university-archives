import os
import sys

def count_in_file(filename, word):
    count = 0
    with open(filename, "r") as file:
        content = file.read()
        lines = content.split("\n")
        for line in lines:
            words = line.split(" ")
            for w in words:
                if w == word:
                    count += 1
            if "\\input" in line:
                l = len(line)
                new_file = line[7:l - 1]
                count += os.spawnv(os.P_WAIT, sys.executable, [sys.executable, "main.py", new_file, word])
    return count

if __name__ == '__main__':
    p = sys.argv[1] 
    s = sys.argv[2]
    result = count_in_file(p, s)
    print(f"słowo '{s}' występuje {result} razy w pliku {p}.")