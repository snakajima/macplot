# -*- coding: utf-8 -*-
# https://dantoudai.wordpress.com/2020/05/24/the-mandelbrot-set-in-python/
import numpy as np
from matplotlib import pyplot as plt

def mandelbrot(num_iter, N, X0, fractal="Mandelbrot"):
    X = np.linspace(X0[0], X0[1], N)
    Y = np.linspace(X0[2], X0[3], N)
    [x, y] = np.meshgrid(X, Y * 1j)
    z = x + y
    c = x + y
    Q = np.zeros([N, N])
     
    for j in range(num_iter):
        index = np.abs(z) < np.inf
        Q[index] = Q[index] + 1
        if fractal == "Julia":
            z = z ** 2 + -0.835 - 0.2321 * 1j
        elif fractal == "Mandelbrot":
            z = z ** 2 + c
     
    plt.figure(figsize = (8, 8))
    plt.pcolormesh(X, Y, Q, cmap = "Greys")
    plt.axis('equal')
    plt.show()
 
def main():
    mandelbrot(10, 1000, [-2.0,2.0,-2.0,2.0], "Mandelbrot")
