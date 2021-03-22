# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import math

def main():
    t = np.arange(0, math.pi * 2, 0.01)
    x = np.cos(t)
    y = np.sin(t)

    plt.figure(figsize=(10, 10))
    plt.plot(x,y)

    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    plt.title("Circle")
