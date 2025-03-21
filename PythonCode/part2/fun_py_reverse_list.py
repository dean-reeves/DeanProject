# fun_py_reverse_list.py

def fun_py_reverse_list(lst):
    return lst[::-1]

def test_reverse_list():
    numbers = [1, 2, 3, 4, 5]
    print(f"Reversed list: {fun_py_reverse_list(numbers)}")

if __name__ == "__main__":
    test_reverse_list()
