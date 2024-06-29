# generate_fibonacci_sequence.py
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    fib_sequence = fibonacci(n)
    print(f"Fibonacci sequence: {fib_sequence}")
