# func_py_calculate_pentagonal_prism_volume.py
import math

def func_py_calculate_pentagonal_prism_volume(side_length, height):
    area_base = (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side_length**2
    return area_base * height

print(func_py_calculate_pentagonal_prism_volume(3, 10))
