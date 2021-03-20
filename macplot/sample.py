from matplotlib import pyplot as plt
import numpy as np
import math #needed for definition of pi

def main(path):
    x = np.arange(0, math.pi * 2 * 10, 0.05)
    y = np.exp(-x * 0.1) * np.sin(x)
    plt.plot(x,y)

    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("Sin wave")

    plt.savefig(path)
