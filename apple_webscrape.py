#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:52:24 2023

@author: avrilguok
"""
'''
datetime: can just input date in any format
'''

import datetime as dt
import yfinance as yf
import pandas as pd



stocks = ["AMZN", "MSFT", "GC=F", "GOOG", "3988.HK"]
start = dt.datetime.today()-dt.timedelta(360)
end = dt.datetime.today()
cl_price = pd.DataFrame() #empty dataframe to store closing prices
#python dictionaries 
ohlcv_data = {}  

# loop over tickers and create data frame 
for ticker in stocks: 
    cl_price[ticker] = yf.download(ticker,start,end)["Adj Close"]
    
for ticker in stocks: 
    ohlcv_data[ticker] = yf.download(ticker,start,end)
    
    
