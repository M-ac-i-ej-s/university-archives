import random
import sys
import threading

sys.setrecursionlimit(10 ** 9)
suma = 0


def sum_all(a: [int]):
    global suma 
    local = 0
    for i in a:
        local += i

    with lockSuma: # blokujemy dostep do zmiennej suma
        suma += local


def sum_all_threaded(matrix, threadsLevel):
    if threadsLevel > 0:
        if len(matrix) > 1:
            q = len(matrix) // 2
            t1 = threading.Thread(target=sum_all_threaded, args=(matrix[:q], threadsLevel - 1))
            t2 = threading.Thread(target=sum_all_threaded, args=(matrix[q:], threadsLevel - 1))
            t1.start() # uruchamiamy watek
            t2.start()
            t1.join() # czekamy na zakonczenie watku
            t2.join()
    else:
        sum_all(matrix)


matrixLength = 1000  
threadsLevel = 4 # poziom rekursji realizowanych wielowątkowo 
lockSuma = threading.Lock()
matrix = [random.randint(0, 100) for i in range(matrixLength)]

sum_all_threaded(matrix, threadsLevel)

if suma == sum(matrix):
    print("Sum correct")
else:
    print("Sum incorrect")

print("Sum: ", suma)
print("Control sum: ", sum(matrix))