# func_py_calculate_mandelbrot_set.py
import numpy as np
import matplotlib.pyplot as plt

def func_py_calculate_mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    x, y = np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height)
    C = np.array([[complex(re, im) for re in x] for im in y])
    Z = np.zeros(C.shape, dtype=complex)
    div_time = np.zeros(C.shape, dtype=int)
    for i in range(max_iter):
        Z = Z**2 + C
        diverge = Z*np.conj(Z) > 4
        div_now = diverge & (div_time == 0)
        div_time[div_now] = i
        Z[diverge] = 2
    plt.imshow(div_time, cmap='hot', extent=(xmin, xmax, ymin, ymax))
    plt.show()

func_py_calculate_mandelbrot_set(-2, 1, -1.5, 1.5, 500, 500, 100)
