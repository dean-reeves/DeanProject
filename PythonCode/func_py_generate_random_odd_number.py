# func_py_generate_random_odd_number.py
import random

def func_py_generate_random_odd_number(start, end):
    return random.choice([i for i in range(start, end+1) if i % 2 != 0])

print(func_py_generate_random_odd_number(1, 100))
