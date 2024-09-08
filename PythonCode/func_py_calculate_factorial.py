# func_py_calculate_factorial.py
def func_py_calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * func_py_calculate_factorial(n - 1)

print(func_py_calculate_factorial(5))
