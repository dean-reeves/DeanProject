# fun_py_count_vowels.py

def fun_py_count_vowels(s):
    return sum(1 for char in s.lower() if char in "aeiou")

def test_count_vowels():
    text = "Hello World"
    print(f"Number of vowels: {fun_py_count_vowels(text)}")

if __name__ == "__main__":
    test_count_vowels()
