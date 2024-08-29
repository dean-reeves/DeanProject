# func_py_find_kaprekar_constant_steps.py
def func_py_find_kaprekar_constant_steps(n):
    KAPREKAR_CONSTANT = 6174
    steps = 0
    while n != KAPREKAR_CONSTANT:
        digits = f"{n:04d}"
        num1 = int("".join(sorted(digits, reverse=True)))
        num2 = int("".join(sorted(digits)))
        n = num1 - num2
        steps += 1
    return steps

print(func_py_find_kaprekar_constant_steps(3524))
