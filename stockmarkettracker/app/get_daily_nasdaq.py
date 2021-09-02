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
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
def main():
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
    stocks_df.to_csv(f"data/{str(datetime.now())}.csv", index=False)
    print(f"Saving to data/{str(datetime.now())}.csv")
    for stock_i in range(len(stocks_df)):
        pass
    
    
        
if __name__ == "__main__":
    main()
