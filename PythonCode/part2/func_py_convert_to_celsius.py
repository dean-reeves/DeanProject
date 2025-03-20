# func_py_convert_to_celsius.py

def func_py_convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def test_convert_to_celsius():
    temperatures = [32, 50, 100]
    for temp in temperatures:
        print(f"{temp} Fahrenheit = {func_py_convert_to_celsius(temp)} Celsius")

if __name__ == "__main__":
    test_convert_to_celsius()
