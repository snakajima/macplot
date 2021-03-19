from matplotlib import pyplot as plt
import numpy as np
import math #needed for definition of pi

def main():
    x = np.arange(0, math.pi*2, 0.05)
    y = np.tan(x)
    plt.plot(x,y)
    plt.xlabel("angle")
    plt.ylabel("Tan value")
    plt.title('Tan wave')
    plt.show()
