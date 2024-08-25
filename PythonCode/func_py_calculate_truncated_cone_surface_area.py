# func_py_calculate_truncated_cone_surface_area.py
import math

def func_py_calculate_truncated_cone_surface_area(radius1, radius2, height):
    slant_height = math.sqrt((radius1 - radius2)**2 + height**2)
    return math.pi * (radius1 + radius2) * slant_height + math.pi * (radius1**2 + radius2**2)

print(func_py_calculate_truncated_cone_surface_area(5, 3, 7))
