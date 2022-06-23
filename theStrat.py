import sys
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

arg1 = sys.argv[1]
tickerName = arg1.upper()
ticker = yf.Ticker(arg1)

today = datetime.now().date().strftime('%Y-%m-%d')
lastYearToday = (datetime.now() - timedelta(days=365)).date().strftime('%Y-%m-%d')
df_price = ticker.history(start=lastYearToday, end=today)
fourDf = df_price[4:]
resultHigh = fourDf.High.values
resultLow = fourDf.Low.values
stratNumbers = []

#Day Before calcs
if resultHigh[0] < resultHigh[1]:
    if resultLow[0] > resultLow[1]:
        print("Day Before: 3")
        dayBefore = 3
        stratNumbers.append(3)
    else:
        print("Day Before: 2")
        dayBefore = 2
        stratNumbers.append(2)
elif resultHigh[0] > resultHigh[1]:
    if resultLow[0] > resultLow[1]:
        print("Day Before: 2")
        dayBefore = 2
        stratNumbers.append(2)
    else:
        print("Day Before: 1")
        dayBefore = 1
        stratNumbers.append(1)

#Yesterday calc
if resultHigh[1] < resultHigh[2]:
    if resultLow[1] > resultLow[2]:
        print("Yesterday: 3")
        yesterday = 3
        stratNumbers.append(3)
    else:
        print("Yesterday: 2")
        yesterday = 2
        stratNumbers.append(2)
elif resultHigh[1] > resultHigh[2]:
    if resultLow[1] > resultLow[2]:
        print("Yesterday: 2")
        yesterday = 2
        stratNumbers.append(2)
    else:
        print("Yesterday: 1")
        yesterday = 1
        stratNumbers.append(1)

#Current Day calc
if resultHigh[2] < resultHigh[3]:
    if resultLow[2] > resultLow[3]:
        print("Current Day: 3")
        current = 3
        stratNumbers.append(3)
    else:
        print("Current Day: 2")
        current = 2
        stratNumbers.append(2)
elif resultHigh[2] > resultHigh[3]:
    if resultLow[2] > resultLow[3]:
        print("Current Day: 2")
        current = 2
        stratNumbers.append(2)
    else:
        print("Current Day: 1")
        current = 1
        stratNumbers.append(1)

print(stratNumbers)

if current == 2:
    if yesterday == 2:
        if dayBefore == 2:
            print("Works")
