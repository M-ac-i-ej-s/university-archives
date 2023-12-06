import threading
import sys
import time

primes = []
threats_amount = 4
n = 10000


def is_prime(n):
    k = int(n ** 0.5) + 1
    for i in range(2, k):
        if n % i == 0:
            return False
    return True


def find_primes(f, t, b):
    p = []
    for i in range(f, t):
        if is_prime(i):
            p.append(i)
    b.wait()
    with lock:
        primes.extend(p)
    return p


threads = []
lock = threading.Lock()
barrier = threading.Barrier(threats_amount)

for i in range(threats_amount):
    threads.append(
        threading.Thread(target=find_primes, args=(i * n // threats_amount, (i + 1) * n // threats_amount, barrier)))
    threads[i].start()
barrier.wait()
print(primes)
sys.exit()