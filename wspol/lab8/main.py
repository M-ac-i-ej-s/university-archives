import time
import random
import math
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


def sum_all_threaded(a, g):
    if g > 0: # sprawdzamy czy nie osiagnelismy poziomu rekurencji
        if len(a) > 1:
            q = len(a) // 2
            t1 = threading.Thread(target=sum_all_threaded, args=(a[:q], g - 1))
            t2 = threading.Thread(target=sum_all_threaded, args=(a[q:], g - 1))
            t1.start() # uruchamiamy watek
            t2.start()
            t1.join() # czekamy na zakonczenie watku
            t2.join()
    else:
        sum_all(a)


matrixLength = 1000  
recursionLevel = 5 
lockSuma = threading.Lock()
a = [random.randint(0, 100) for i in range(matrixLength)]

sum_all_threaded(a, recursionLevel)

if suma == sum(a):
    print("Sum correct")
else:
    print("Sum incorrect")

print("Sum: ", suma)
print("Control sum: ", sum(a))