# func_py_generate_random_prime_number.py
import random

def func_py_is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def func_py_generate_random_prime_number(start, end):
    primes = [i for i in range(start, end + 1) if func_py_is_prime(i)]
    return random.choice(primes) if primes else None

print(func_py_generate_random_prime_number(1, 100))
