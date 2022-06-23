import sys
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

import yfinance as yf

arg1 = sys.argv[1]
tickerName = arg1.upper()
ticker = yf.Ticker(arg1)

today = datetime.now().date().strftime('%Y-%m-%d')
lastYearToday = (datetime.now() - timedelta(days=365)).date().strftime('%Y-%m-%d')
df_price = ticker.history(start=lastYearToday, end=today)
fourDf = df_price[:4]
resultHigh = fourDf.High.values
resultLow = fourDf.Low.values

#Day Before calcs
if resultHigh[0] < resultHigh[1]:
    if resultLow[0] > resultLow[1]:
        dayBefore = 3
    else:
        dayBefore = 2
elif resultHigh[0] > resultHigh[1]:
    if resultLow[0] > resultLow[1]:
        dayBefore = 2
    else:
        dayBefore = 1

#Yesterday calc
if resultHigh[1] < resultHigh[2]:
    if resultLow[1] > resultLow[2]:
        yesterday = 3
    else:
        yesterday = 2
elif resultHigh[1] > resultHigh[2]:
    if resultLow[1] > resultLow[2]:
       yesterday = 2
    else:
        yesterday = 1

#Current Day calc
if resultHigh[2] < resultHigh[3]:
    if resultLow[2] > resultLow[3]:
        current = 3
    else:
        current = 2
elif resultHigh[2] > resultHigh[3]:
    if resultLow[2] > resultLow[3]:
        current = 2
    else:
        current = 1

if current == 2:
    if yesterday == 2:
        if dayBefore == 2:
            print("Works")
