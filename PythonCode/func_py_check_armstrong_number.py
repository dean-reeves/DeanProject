# func_py_check_armstrong_number.py
def func_py_check_armstrong_number(n):
    digits = list(map(int, str(n)))
    return n == sum(d ** len(digits) for d in digits)

print(func_py_check_armstrong_number(153))
