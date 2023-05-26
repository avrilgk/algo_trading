#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 15:59:43 2023

@author: avrilguok
"""

import datetime as dt
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

stocks = ["S51.SI", "MSFT", "TSM", "3988.HK"]
start = dt.datetime(2022, 5, 1)
end = dt.datetime(2023, 5, 26)
cl_price = pd.DataFrame() 
ohlcv_data = {}


for ticker in stocks:
    cl_price[ticker] = yf.download(ticker, start, end)["Adj Close"]
    

daily_return = cl_price.pct_change()


fig, ax = plt.subplots()
plt.style.available
plt.style.use('ggplot')
ax.set(title='Daily returns', xlabel='Stocks', ylabel='Mean Return')
plt.bar(x=daily_return.columns, height=daily_return.mean(), color=['gray'])
#plt.bar(x=daily_return.columns, height=daily_return.std())