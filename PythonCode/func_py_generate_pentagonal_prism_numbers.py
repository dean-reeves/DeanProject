# func_py_generate_pentagonal_prism_numbers.py
def func_py_generate_pentagonal_prism_numbers(n):
    return [i * (5 * i - 2) for i in range(1, n + 1)]

print(func_py_generate_pentagonal_prism_numbers(10))
