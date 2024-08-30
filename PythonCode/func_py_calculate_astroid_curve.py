# func_py_calculate_astroid_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_astroid_curve(a, points):
    t = np.linspace(0, 2 * np.pi, points)
    x = a * np.cos(t)**3
    y = a * np.sin(t)**3
    plt.plot(x, y)
    plt.title("Astroid Curve")
    plt.show()

func_py_calculate_astroid_curve(5, 1000)
