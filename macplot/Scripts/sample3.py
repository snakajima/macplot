# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import math #needed for definition of pi

def main():
    sd = 10.0
    average = 50.0
    x = np.arange(average - sd * 5, average + sd * 5, 1)
    y = np.exp(-np.power((x - average)/sd,2)/2) / (sd * np.sqrt(2 * math.pi))
    plt.bar(x,y,1)

    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("Normal Disribution")
