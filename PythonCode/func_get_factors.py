# func_get_factors.py
def func_get_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]

print(func_get_factors(30))
