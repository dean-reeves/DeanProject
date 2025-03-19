# func_py_most_frequent.py

from collections import Counter

def func_py_most_frequent(lst):
    return Counter(lst).most_common(1)[0][0]

def test_most_frequent():
    numbers = [1, 3, 2, 3, 4, 3, 5]
    print(f"Most frequent element: {func_py_most_frequent(numbers)}")

if __name__ == "__main__":
    test_most_frequent()
