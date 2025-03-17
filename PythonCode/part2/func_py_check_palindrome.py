# func_py_check_palindrome.py

def func_py_check_palindrome(s):
    return s == s[::-1]

def test_check_palindrome():
    words = ["madam", "racecar", "hello", "python"]
    for word in words:
        print(f"'{word}' is a palindrome: {func_py_check_palindrome(word)}")

if __name__ == "__main__":
    test_check_palindrome()
