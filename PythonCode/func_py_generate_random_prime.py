# func_py_generate_random_prime.py
import random

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def func_py_generate_random_prime(start, end):
    primes = [i for i in range(start, end + 1) if is_prime(i)]
    return random.choice(primes)

print(func_py_generate_random_prime(10, 50))
