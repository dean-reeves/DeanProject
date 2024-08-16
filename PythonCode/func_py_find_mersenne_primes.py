# func_py_find_mersenne_primes.py
def func_py_find_mersenne_primes(limit):
    primes = []
    for num in range(2, limit):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            mersenne_candidate = 2**num - 1
            if all(mersenne_candidate % j != 0 for j in range(2, int(mersenne_candidate**0.5) + 1)):
                primes.append(mersenne_candidate)
    return primes

print(func_py_find_mersenne_primes(31))
