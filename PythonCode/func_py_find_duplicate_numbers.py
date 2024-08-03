# func_py_find_duplicate_numbers.py
def func_py_find_duplicate_numbers(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

print(func_py_find_duplicate_numbers([1, 2, 2, 3, 4, 4, 5]))
