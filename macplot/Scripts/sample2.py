# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import math #needed for definition of pi

def main():
    x = np.arange(0, math.pi * 2 * 10, 0.05)
    y = np.exp(-x * 0.2) * np.sin(x)
    plt.plot(x,y)

    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("Decaying Sin Wave")
