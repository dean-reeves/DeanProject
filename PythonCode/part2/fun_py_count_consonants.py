# fun_py_count_consonants.py

def fun_py_count_consonants(s):
    return sum(1 for char in s.lower() if char.isalpha() and char not in "aeiou")

def test_count_consonants():
    text = "Hello World"
    print(f"Number of consonants: {fun_py_count_consonants(text)}")

if __name__ == "__main__":
    test_count_consonants()
