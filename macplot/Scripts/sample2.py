# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import math

def main():
    x = np.arange(0, math.pi * 2 * 7, 0.05)
    y = 0.5 * np.exp(-x * 0.1) * np.sin(x * 10) + np.sin(x)
    plt.plot(x,y)

    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("Decaying Sin Wave with another Sin Wave")
