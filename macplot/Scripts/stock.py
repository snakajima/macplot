# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import math #needed for definition of pi
import csv
import urllib2
import datetime

def main():
    symbol = "TSLA"
    today = (datetime.datetime.utcnow() - datetime.datetime(1970,1,1)).days
    length = 365
    params = {
        "period1": str((today - length)  * 24 * 60 * 60),
        "period2": str(today * 24 * 60 * 60),
        "interval": "1wk",
        "includeAdjustedClose": "true"
    }
    query = "&".join(map(lambda key: "=".join([key, params[key]]), params))
    url = "https://query1.finance.yahoo.com/v7/finance/download/"
    response = urllib2.urlopen(url + symbol + "?" + query)
    rows = map(lambda x: x, csv.DictReader(response))
    
    closes = map(lambda x: x["Close"], rows)
    indeces = np.arange(len(closes))
    ticks = filter(lambda x: x % (len(closes) / 10) == 0, indeces)
    plt.xticks(ticks, map(lambda x: rows[x]["Date"], ticks), rotation=30, ha='right')
    plt.plot(indeces, closes)
    plt.title("Historical Stock Price: " + symbol)
