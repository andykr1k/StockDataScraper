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
df_price = ticker.history(start=lastYearToday, end=today).Close

plt.figure()
plt.plot(df_price)
plt.ylabel('Price')
plt.xlabel('Date')
plt.title(tickerName + ' Price Plot')
plt.show()
