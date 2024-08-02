# func_py_generate_random_number_list.py
import random

def func_py_generate_random_number_list(size, start, end):
    return [random.randint(start, end) for _ in range(size)]

print(func_py_generate_random_number_list(5, 1, 100))
