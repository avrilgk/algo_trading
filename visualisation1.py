#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 11:45:23 2023

@author: avrilguok
"""
import datetime as dt
import yfinance as yf
import pandas as pd

stocks = ["S51.SI", "MSFT", "TSM", "3988.HK"]
start = dt.datetime(2022, 5, 1)
end = dt.datetime(2023, 5, 26)
cl_price = pd.DataFrame() 
ohlcv_data = {}


for ticker in stocks:
    cl_price[ticker] = yf.download(ticker, start, end)["Adj Close"]
    

daily_return = cl_price.pct_change()

#pandas plot documentation 
cl_price.plot(subplots=True, layout=(2,2), title="Stock Price Evolution", grid=True)

daily_return.plot(subplots=True, layout=(2,2), title="Daily Returns May Evolution", grid=True)

  
