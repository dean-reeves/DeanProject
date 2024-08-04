# func_py_get_positive_numbers.py
def func_py_get_positive_numbers(lst):
    return [i for i in lst if i > 0]

print(func_py_get_positive_numbers([-1, 2, -3, 4, -5, 6]))
