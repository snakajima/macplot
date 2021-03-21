# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import math #needed for definition of pi
import csv
import urllib2

def main():
    url = 'https://query1.finance.yahoo.com/v7/finance/download/TSLA?period1=1584794842&period2=1616330842&interval=1wk&events=history&includeAdjustedClose=true'
    response = urllib2.urlopen(url)
    cr = csv.DictReader(response)
    rows = map(lambda x: x, cr)
    dates = map(lambda x: x["Date"], rows)
    closes = map(lambda x: x["Close"], rows)
    indeces = np.arange(len(dates))
    ticks = filter(lambda x: x % 5 == 0, indeces)
    plt.xticks(ticks, map(lambda x: dates[x], ticks), rotation=30, ha='right')
    plt.plot(indeces, closes)
    plt.title("Historical Stock Price: TSLA")
    
