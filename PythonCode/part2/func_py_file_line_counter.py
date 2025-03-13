# func_py_file_line_counter.py
def func_py_file_line_counter(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return sum(1 for _ in file)
    except FileNotFoundError:
        return "File not found"

print(func_py_file_line_counter("example.txt"))
