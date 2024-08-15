# func_py_generate_centered_hexagonal_numbers.py
def func_py_generate_centered_hexagonal_numbers(n):
    return [3 * i * (i - 1) + 1 for i in range(1, n + 1)]

print(func_py_generate_centered_hexagonal_numbers(10))
