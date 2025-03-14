# func_py_find_missing_number.py

def func_py_find_missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

def test_find_missing_number():
    test_cases = [
        ([1, 2, 4, 5, 6], 6),
        ([3, 7, 1, 2, 8, 4, 5], 8),
        ([1, 3, 4, 5], 5),
    ]
    for arr, n in test_cases:
        print(f"Missing number in {arr}: {func_py_find_missing_number(arr, n)}")

if __name__ == "__main__":
    test_find_missing_number()
