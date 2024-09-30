# func_py_find_greatest_common_divisor.py
def func_py_find_greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a
