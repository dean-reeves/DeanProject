# func_py_generate_palindromic_prime_numbers.py
def func_py_generate_palindromic_prime_numbers(limit):
    def is_prime(n):
        return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    return [n for n in range(2, limit + 1) if is_prime(n) and is_palindrome(n)]

print(func_py_generate_palindromic_prime_numbers(1000))
