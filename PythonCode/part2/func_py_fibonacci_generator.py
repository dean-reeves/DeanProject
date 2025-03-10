# func_py_fibonacci_generator.py
def func_py_fibonacci_generator(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(func_py_fibonacci_generator(10))
