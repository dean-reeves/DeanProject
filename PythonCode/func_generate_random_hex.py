# func_generate_random_hex.py
import random

def func_generate_random_hex(length):
    return ''.join(random.choice('0123456789ABCDEF') for i in range(length))

print(func_generate_random_hex(8))
