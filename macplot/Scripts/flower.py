# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import math

def main():
    t = np.arange(0, math.pi * 2, 0.01)
    r = (1 + 0.1 *np.abs( np.sin(t * 8)))
    x = r * np.cos(t)
    y = r * np.sin(t)
    plt.plot(x,y)

    plt.xlim([-2.5, 2.5])
    plt.ylim([-2, 2])
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Flower")
