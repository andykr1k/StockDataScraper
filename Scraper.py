import sys
import pandas as pd
import matplotlib as plt
from datetime import datetime

import yfinance as yf


#ticker = sys.argv[1]

def get_close_price(ticker):
    stock_info = yf.Ticker(ticker).info
    close_price = stock_info['regularMarketPrice']
    return close_price

def get_open_price(ticker):
    stock_info = yf.Ticker(ticker).info
    open_price = stock_info['regularMarketOpen']
    return open_price

def get_strat(ticker):
    stringStrat = ""

    stock_info = yf.Ticker(ticker).info

    close_price = get_close_price(ticker)
    open_price = get_open_price(ticker)

    if close_price == open_price:
        stringStrat = "No Change"
    elif close_price > open_price:
        stringStrat = "Bullish"
    else:
        stringStrat = "Bearish"

    return stringStrat

msft = yf.Ticker("MSFT")

stockinfo = msft.info

#for key,value in stockinfo.items():
    #print(key,":",value)

#numshares = msft.info['sharesOutstanding']
#print(numshares)

df = msft.dividends
print(df)

#print("Close Price: ", get_close_price(ticker))
#print("Open Price: ", get_open_price(ticker))
#print(get_strat(ticker))

