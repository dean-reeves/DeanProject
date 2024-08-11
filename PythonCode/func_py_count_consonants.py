# func_py_count_consonants.py
def func_py_count_consonants(text):
    return sum(1 for char in text.lower() if char in 'bcdfghjklmnpqrstvwxyz')

print(func_py_count_consonants("Hello World"))
