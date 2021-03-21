# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import math #needed for definition of pi
import csv
import urllib2

def main():
    symbol = "TSLA"
    start = 1584794842
    length = 365 * 24 * 60 * 60
    params = {
        "period1": str(start),
        "period2": str(start + length),
        "interval": "1wk",
        "includeAdjustedClose": "true"
    }
    query = "&".join(map(lambda key: "=".join([key, params[key]]), params))
    print(1584794842 / 24 / 60 / 60)

    url = "https://query1.finance.yahoo.com/v7/finance/download/"
    response = urllib2.urlopen(url + symbol + "?" + query)
    cr = csv.DictReader(response)
    rows = map(lambda x: x, cr)
    
    closes = map(lambda x: x["Close"], rows)
    indeces = np.arange(len(closes))
    ticks = filter(lambda x: x % 5 == 0, indeces)
    plt.xticks(ticks, map(lambda x: rows[x]["Date"], ticks), rotation=30, ha='right')
    plt.plot(indeces, closes)
    plt.title("Historical Stock Price: " + symbol)
