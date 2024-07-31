# func_py_generate_random_string.py
import random
import string

def func_py_generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

print(func_py_generate_random_string(8))
