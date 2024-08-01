# func_py_count_vowels.py
def func_py_count_vowels(string):
    return sum(1 for char in string if char.lower() in 'aeiou')

print(func_py_count_vowels("Hello, World!"))
