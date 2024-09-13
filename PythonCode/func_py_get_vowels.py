# func_py_get_vowels.py
def func_py_get_vowels(s):
    vowels = "aeiou"
    return [char for char in s if char.lower() in vowels]

print(func_py_get_vowels("Programming"))
