# fun_py_generate_random_password.py
import random
import string

def fun_py_generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

print(fun_py_generate_random_password(10))
