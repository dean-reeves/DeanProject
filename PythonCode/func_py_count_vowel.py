# func_py_count_vowel.py
def func_py_count_vowels(s):
    return sum(1 for char in s.lower() if char in 'aeiou')

print(func_py_count_vowels("Hello World"))
