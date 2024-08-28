# func_py_generate_automorphic_numbers.py
def func_py_generate_automorphic_numbers(limit):
    return [n for n in range(1, limit) if str(n*n).endswith(str(n))]

print(func_py_generate_automorphic_numbers(1000))
