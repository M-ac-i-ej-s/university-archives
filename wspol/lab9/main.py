import threading
from threading import Barrier
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(start, end, result_list, barrier):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    result_list.extend(primes)
    barrier.wait()

def main():
    start_range = 2
    end_range = 10000
    num_threads = 4  # Możesz dostosować ilość wątków według własnych potrzeb

    # Inicjalizacja bariery z ilością wątków
    barrier = Barrier(num_threads)

    # Przygotowanie listy wynikowej do przechowywania liczb pierwszych
    result_list = []

    # Rozbicie przedziału na podprzedziały dla każdego wątku
    step = (end_range - start_range + 1) // num_threads
    ranges = [(i, i + step - 1) for i in range(start_range, end_range + 1, step)]

    # Tworzenie i uruchamianie wątków
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=find_primes, args=(ranges[i][0], ranges[i][1], result_list, barrier))
        threads.append(thread)
        thread.start()

    # Czekanie na zakończenie wszystkich wątków
    for thread in threads:
        thread.join()

    # Wyświetlanie wyników
    print("Liczby pierwsze w przedziale", start_range, "do", end_range, "to:", result_list)

if __name__ == "__main__":
    main()