# func_py_check_prime_number.py
def func_py_check_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(func_py_check_prime_number(29))
