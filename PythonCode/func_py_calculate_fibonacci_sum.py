# func_py_calculate_fibonacci_sum.py
def func_py_calculate_fibonacci_sum(n):
    a, b = 0, 1
    fib_sum = 0
    for _ in range(n):
        fib_sum += a
        a, b = b, a + b
    return fib_sum

print(func_py_calculate_fibonacci_sum(6))
