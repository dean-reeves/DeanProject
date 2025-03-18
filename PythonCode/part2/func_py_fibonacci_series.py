# func_py_fibonacci_series.py

def func_py_fibonacci_series(n):
    fib = [0, 1]
    for _ in range(n - 2):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

def test_fibonacci_series():
    print(f"Fibonacci series (10): {func_py_fibonacci_series(10)}")

if __name__ == "__main__":
    test_fibonacci_series()
