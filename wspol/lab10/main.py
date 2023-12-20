import math
import time
import multiprocessing

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes_up_to_sqrt(end):
    primes = []
    sqrt_end = int(math.sqrt(end))
    for num in range(2, sqrt_end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def find_twins_in_range(start, end, primes):
    twins = []
    for num in range(start, end + 1):
        if num < 2:
            continue
        is_prime_num = True
        for prime in primes:
            if prime > math.sqrt(num):
                break
            if num % prime == 0:
                is_prime_num = False
                break
        if is_prime_num:
            if num + 2 <= end and is_prime(num + 2):
                twins.append((num, num + 2))
    return twins

def find_twins_parallel(start, end, primes, processes):
    step = (end - start + 1) // processes
    ranges = [(start + i * step, start + (i + 1) * step - 1) for i in range(processes)]

    with multiprocessing.Pool(processes=processes) as pool:
        results = pool.starmap(find_twins_in_range, [(s, e, primes) for s, e in ranges])

    return [twin for sublist in results for twin in sublist]

if __name__ == "__main__":
    start_time = time.time()

    end_range = 10000
    primes_up_to_sqrt = generate_primes_up_to_sqrt(end_range)

    seq_twins = find_twins_in_range(1, end_range, primes_up_to_sqrt)

    seq_time = time.time() - start_time
    print(f"Sequential Time: {seq_time:.4f}s")
    print(f"Sequential twins: {seq_twins}")
    print(f"Number of sequential twins: {len(seq_twins)}")

    start_time = time.time()

    processes = 4
    parallel_twins = find_twins_parallel(1, end_range, primes_up_to_sqrt, processes)

    parallel_time = time.time() - start_time
    print(f"Parallel Time ({processes} processes): {parallel_time:.4f}s")
    print(f"parraler twins (parallel); {parallel_twins}")
    print(f"Number of parallel twins: {len(parallel_twins)}")

    print(f"Speedup: {seq_time / parallel_time:.4f}")