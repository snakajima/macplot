# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import csv
import urllib2
import datetime

def main():
    symbol = "TSLA"
    long = 30
    short = 15
    
    today = (datetime.datetime.utcnow() - datetime.datetime(1970,1,1)).days
    length = 365 + long
    params = {
        "period1": str((today - length)  * 24 * 60 * 60),
        "period2": str(today * 24 * 60 * 60),
        "interval": "1d", # or 1wk
        "includeAdjustedClose": "true"
    }
    query = "&".join(map(lambda key: "=".join([key, params[key]]), params))
    url = "https://query1.finance.yahoo.com/v7/finance/download/"
    response = urllib2.urlopen(url + symbol + "?" + query)
    rows = map(lambda x: x, csv.DictReader(response))
    closes = map(lambda x: float(x["Close"]), rows)

    cumsum = np.cumsum(closes)
    averageLong = (cumsum[long:] - cumsum[:-long]) / float(long)
    averageShort = (cumsum[short:] - cumsum[:-short]) / float(short)

    indeces = np.arange(len(averageLong))
    ticks = filter(lambda x: x % (len(averageLong) / 10) == 0, indeces)
    plt.xticks(ticks, map(lambda x: rows[x]["Date"], ticks), rotation=30, ha='right')
    plt.plot(indeces, closes[long:])
    plt.plot(indeces, averageLong, label=str(long)+"-day average")
    plt.plot(indeces, averageShort[(long-short):], label=str(short)+"-day average")
    plt.legend(loc='best')
    plt.title("Historical Stock Price: " + symbol)
