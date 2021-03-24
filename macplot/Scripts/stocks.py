# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import csv
import urllib2
import datetime

def query(symbol):
    today = (datetime.datetime.utcnow() - datetime.datetime(1970,1,1)).days
    length = 365 * 5
    params = {
        "period1": str((today - length)  * 24 * 60 * 60),
        "period2": str(today * 24 * 60 * 60),
        "interval": "1d", # or 1wk
        "includeAdjustedClose": "true"
    }
    query = "&".join(map(lambda key: "=".join([key, params[key]]), params))
    url = "https://query1.finance.yahoo.com/v7/finance/download/"
    response = urllib2.urlopen(url + symbol + "?" + query)
    return map(lambda x: x, csv.DictReader(response))

def closes(rows):
    firstValue = float(rows[0]["Close"])
    return map(lambda x: float(x["Close"]) / firstValue, rows)

def main():
    rows = query("GOOG")
    indeces = np.arange(len(rows))
    ticks = filter(lambda x: x % (len(rows) / 10) == 0, indeces)
    plt.xticks(ticks, map(lambda x: rows[x]["Date"], ticks), rotation=30, ha='right')
    plt.plot(indeces, closes(rows))
    plt.plot(indeces, closes(query("AAPL")))
    plt.plot(indeces, closes(query("MSFT")))
    plt.plot(indeces, closes(query("AMZN")))
    plt.title("Historical Stock Price")
