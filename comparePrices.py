import sys
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import yfinance as yf

arguments = sys.argv
tickers = []
titleName = ""

for argument in arguments:
    if argument != "comparePrices.py":
        tickers.append(argument.upper())
        titleName += argument.upper() + " "

df = pd.DataFrame()
today = datetime.now().date().strftime('%Y-%m-%d')
lastYearToday = (datetime.now() - timedelta(days=365)).date().strftime('%Y-%m-%d')


for ticker in tickers:
    df[ticker] = yf.Ticker(ticker).history(start=lastYearToday, end=today).Close

plt.figure()
plt.plot(df)
plt.ylabel('Price')
plt.xlabel('Date')
plt.title(titleName + ' Price Comparison')
plt.show()
