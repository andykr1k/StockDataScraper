import yfinance as yf
import sys

ticker = sys.argv[1]

def get_close_price(ticker):
    stock_info = yf.Ticker(ticker).info
    close_price = stock_info['regularMarketPrice']
    return close_price

def get_open_price(ticker):
    stock_info = yf.Ticker(ticker).info
    open_price = stock_info['regularMarketOpen']
    return open_price

def get_strat(ticker):
    stock_info = yf.Ticker(ticker).info
    close_price = get_close_price(ticker)
    open_price = get_open_price(ticker)
    if close_price == open_price:
        print('The stock is flat')
    elif close_price > open_price:
        print('The stock is up')
    else:
        print('The stock is down')

print(get_close_price(ticker))
print(get_open_price(ticker))
print(get_strat(ticker))
