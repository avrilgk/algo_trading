#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 10:25:53 2023

@author: avrilguok
"""

import datetime as dt
import yfinance as yf
import pandas as pd

stocks = ["S51.SI", "C6L.SI", "TSM", "3988.HK"]
start = dt.datetime(2023, 5, 1)
end = dt.datetime(2023, 5, 31)
cl_price = pd.DataFrame() 
ohlcv_data = {}


for ticker in stocks:
    cl_price[ticker] = yf.download(ticker, start, end)["Adj Close"]
    

#cl_price.dropna(axis=0, how='any', inplace=True)


cl_price.mean()
cl_price.std()
cl_price.median()
cl_price.describe()
cl_price.tail(8)

#any QF analysis or discipline relies on asset returns and NOT asset price 
#for financial time series, what we are looking for is returns, not the actual value 

daily_return = cl_price.pct_change()*100
#cl_price/cl_price.shift(-1)

daily_return.mean()
daily_return.std()
#higher std, higher volatility


#usually need to calculate rolling mean of a given time series
#finding mean of a given window (rolling window of 10l)
#benefit: gives a much smoother curve 

#finding rolling mean of window of 10 days 
#simple mean -- equal weightage for each number
r_mean= daily_return.rolling(window=7).mean()
r_std= daily_return.rolling(window=7).std()
r_med= daily_return.rolling(window=7).median()

#typically in QF, more weightage to more recent values
#use exponential moving average -- exponential weighting/smoothing
#smoothing techniques: decay factor 
#decay: importance of value decaying going from more recent to previous

ewm_mean = daily_return.ewm(com=7, min_periods=7).mean()

