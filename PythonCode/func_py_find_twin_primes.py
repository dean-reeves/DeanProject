# func_py_find_twin_primes.py
def func_py_find_twin_primes(limit):
    primes = []
    for num in range(2, limit):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
    twin_primes = [(p, p + 2) for p in primes if p + 2 in primes]
    return twin_primes

print(func_py_find_twin_primes(100))
