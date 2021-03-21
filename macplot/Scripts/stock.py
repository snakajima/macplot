# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import math #needed for definition of pi
import csv
import urllib2

def main():
    symbol = "TSLA"
    params = {
        "period1": "1584794842",
        "period2": "1616330842",
        "interval": "1wk",
        "includeAdjustedClose": "true"
    }
    query = "&".join(map(lambda key: "=".join([key, params[key]]), params))
    print(query)

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

    
