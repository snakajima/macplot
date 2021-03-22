# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import poisson # definition of poisson
import math #needed for definition of factorial
# poisson distribution
def main():
    x = np.arange(20)
    mu_list = [1, 3, 5, 10]
    for idx, mu in enumerate(mu_list):
        # plt.plot(x, poisson.pmf(k=x, mu=mu), 'o-', label='mu={}'.format(mu))
        y = (mu**x * np.e**(-mu))/np.vectorize(np.math.factorial)(x)
        plt.plot(x, y, 'o-', label='mu={}'.format(mu))
    plt.legend()
    plt.xlabel("Num. of calls wihtin a hour")
    plt.ylabel("probability")
