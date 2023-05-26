#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup

income_statement = {}

url = "https://sg.finance.yahoo.com/quote/AAPL/financials?p=AAPL"
headers = {"User-Agent": "Chrome/113.0.5672.126"}
page = requests.get(url, headers=headers)
page_content = page.content
soup = BeautifulSoup(page_content, "html.parser")
tabl = soup.find_all("div", {"class": "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})

for t in tabl:
    rows = t.find_all("div", {"class": "D(tbr) fi-row Bgc($hoverBgColor):h"})
    for row in rows:
        row_text = row.get_text(separator="_")
        row_data = row_text.split("_")
        if len(row_data) >= 2:
            income_statement[row_data[0]] = row_data[1]
        else:
            print("Incomplete data for row:", row_text)


        


