#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 16:52:01 2021

@author: niravshah
"""

import requests, json
import pandas as pd
import time
from collections import defaultdict
from selenium import webdriver
import os
from datetime import datetime
#from pyvirtualdisplay import Display
from app.models import stocks

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
def main():
    print("Starting Display")
    
    # display = Display(visible=0, size=(800, 800))  
    # display.start()
    print("Running", datetime.now())
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("window-size=800,1600")
    #chrome_options.add_argument("--incognito")
   # chrome_options.add_argument('--headless')

    browser = webdriver.Chrome(executable_path=PROJECT_ROOT+"/chromedriver",options =chrome_options )
    url = "https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=25&offset=7350&download=true"
    browser.get(url)

    text = browser.find_element_by_tag_name('body').text
    browser.close()

    json_ = json.loads(text)

    stocks_df = pd.DataFrame.from_dict(json_['data']['rows'])
    print(stocks_df.columns)

    for stock_i in range(len(stocks_df)):
        date            = datetime.now()
        stock_ticker    = stocks_df['symbol'][stock_i]
        stock_name      = stocks_df['name'][stock_i]
        stocks_price    = float(stocks_df['lastsale'][stock_i].strip('$'))
        stock_time      = 1 if datetime.now().time() > datetime.strptime("13:30","%H:%M").time() else 0
        stock_volume    = float(stocks_df['volume'][stock_i])

        if stock_time == 1:
            stock_date = datetime.strptime(str(datetime.now().date())+" 16:00","%Y-%m-%d %H:%M")
        else:
            stock_date = datetime.strptime(str(datetime.now().date())+" 09:30","%Y-%m-%d %H:%M")
        pass

        stock = stocks(date        = stock_date,
                        stock       = stock_name,
                        ticker      = stock_ticker,
                        closePrice  = stocks_price,
                        volume      = stock_volume)
        stock.save()
    
    
        
if __name__ == "__main__":
    main()
