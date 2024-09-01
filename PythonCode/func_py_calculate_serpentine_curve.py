# func_py_calculate_serpentine_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_serpentine_curve(a, points):
    t = np.linspace(-2, 2, points)
    x = a * t / (1 + t**2)
    y = a * t**2 / (1 + t**2)
    plt.plot(x, y)
    plt.title("Serpentine Curve")
    plt.show()

func_py_calculate_serpentine_curve(5, 1000)
