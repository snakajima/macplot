# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import math

def main():
    x = np.arange(20)
    mu_list = [1, 3, 5, 10]
    for mu in mu_list:
        y = (mu**x * np.e**(-mu))/np.vectorize(np.math.factorial)(x)
        plt.plot(x, y, 'o-', label='mu={}'.format(mu))

    plt.legend()
    plt.xlabel("Num. of calls wihtin a hour")
    plt.ylabel("Probability")
