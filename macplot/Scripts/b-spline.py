# -*- coding: utf-8 -*-
# https://github.com/kawache/Python-B-spline-examples
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

def main():
    ctr =np.array( [(3 , 1), (2.5, 4), (0, 1), (-2.5, 4),
                    (-3, 0), (-2.5, -4), (0, -1), (2.5, -4), (3, -1)])

    x=ctr[:,0]
    y=ctr[:,1]

    tck,u = interpolate.splprep([x,y],k=3,s=0)
    u=np.linspace(0,1,num=200,endpoint=True)
    out = interpolate.splev(u,tck)

    plt.figure()
    plt.plot(x, y, 'ro', out[0], out[1], 'b')
    plt.legend(['Points', 'Interpolated B-spline', 'True'],loc='best')
    plt.axis([min(x)-1, max(x)+1, min(y)-1, max(y)+1])
    plt.title('B-Spline interpolation')
