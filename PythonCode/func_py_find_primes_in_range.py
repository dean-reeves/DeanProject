# func_py_find_primes_in_range.py
def func_py_find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes

print(func_py_find_primes_in_range(10, 50))
