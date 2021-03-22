# -*- coding: utf-8 -*-
# https://stackoverflow.com/questions/15024461/plot-mandelbrot-with-matplotlib-pyplot-numpy-python
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def main():
    x, y = np.ogrid[-2:1:500j, -1.5:1.5:500j]

    # Increase this to improve the shape of the fractal
    iterations = 20

    c = x + 1j*y

    z = reduce(lambda x, y: x**2 + c, [1] * iterations, c)

    plt.figure(figsize=(10, 10))
    plt.imshow(np.angle(z));

    plt.figure(figsize=(10, 10))
    plt.imshow(np.log(np.abs(z)));
