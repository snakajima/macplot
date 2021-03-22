# -*- coding: utf-8 -*-
# https://high-python-ext-1-doing-math.readthedocs.io/en/latest/chapter6.html
import matplotlib.pyplot as plt
import random

def transformation_1(p):
    x = p[0]
    y = p[1]
    return x + 1, y - 1
def transformation_2(p):
    x = p[0]
    y = p[1]
    return x + 1, y + 1
def transform(p):
    # List of transformation functions
    transformations = [transformation_1, transformation_2]
    # Pick a random transformation function and call it
    t = random.choice(transformations)
    x, y = t(p)
    return x, y
def build_trajectory(p, n):
    x = [p[0]]
    y = [p[1]]
    for i in range(n):
        p = transform(p)
        x.append(p[0])
        y.append(p[1])
    return x, y

def main():
    p = (1, 1)
    n = 3000
    x, y = build_trajectory(p, n)
    plt.plot(x, y)
