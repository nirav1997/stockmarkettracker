#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 21:15:49 2021

@author: niravshah
"""

import requests, json
import pandas as pd
import time
from datetime import datetime
from collections import defaultdict
import time
from app.models import stocks
import pathlib
root_path = str(pathlib.Path(__file__).parent.resolve())
API_KEYS    = [ 
                "HV60OTX0HG2MLY7X", 
                "8CNQQUK9POAG5ACR", 
                "EYTC7N86HXEB8BER", 
                "PINQUEBAQP18A0ZJ", 
                "JLXKM4EPZRXZSQ41", 
                "LI7Z53AMKC2310BK", 
                "UDN3EOCGOG9TEXY4", 
                "HM6LG8T6J4977771",
                "YHGCFR06WWV0R1F7", 
                "QDC6VHPTWNGT6KEI", 
                "K3YUUIJKLUV4ZNLA", 
                "RUUBTJNDIX34LT9", 
                "CKJJPQWQECIUV4VM", 
                "0YON0P5638Z81NL1", 
                "0DZGHP62J3Q3RRAA",
                "ZGJHYAEXYUYYKFCH",
                "MRCIC8V7GQNBR35R",
                "JZMSDH87JNLN1SNU",
                "UZBZQFRXJVKYERK2",
                "ZJFW9DY4J6FWI64X",
                "12X5675BVHOW95X0",
                "4HO8XONH3TFPH1QV",
                "R674II7I34UCR9BN",
                "B43RXJX3KHGCF5D6",
                "35IXXYZWIGZNTJVB",
                "UCRL9GF00G18CUVN",
                "U4V1CN8NQ5P3R9N0",
                "IB6Z25D0I5AMXZP3",
                "CL5NSFQ3F9L0DCSG",
            ]

def main():
    #time.sleep(60)
    print("Get All Stocks which data is already available")
    stocks_file = open(f"{root_path}/stocks.txt")
    stocks_list = stocks_file.read().split("\n")
    stocks_file.close()

    df = pd.read_csv(f"{root_path}/NASDAQ.csv")
    key_utils = defaultdict(int)
    key = API_KEYS.pop()
    total = 0
    
    for ind in range(len(df)):
        
        if total == 1:
            break

        if df['Symbol'][ind] in stocks_list:
                continue

        try:
            t0 = time.time()
            ticker = df['Symbol'][ind]
            if ind % 5 == 0:
                time.sleep(60)
            if ind%400 == 0:
                key = API_KEYS.pop()
            print(ind, ticker, key)
            url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&interval=5min&apikey={key}&outputsize=full"
            df_ = pd.read_csv(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&interval=5min&apikey={key}&datatype=csv&outputsize=full")

            df_.to_csv(f"{root_path}/data/{ticker.replace('/','_')}.csv", index=False)

            ####### Save to models ########
            stockName   = df['Name'][ind]
            stockTicker = ticker
            
            stocks_file = open(f"{root_path}/stocks.txt", "a")
            stocks_file.write(f"{stockTicker}\n")
            stocks_file.close()

            for i in range(len(df_)):
                date        = datetime.strptime(df_['timestamp'][i], '%Y-%m-%d')
                openPrice   = df_['open'][i]
                closePrice  = df_['close'][i]
                highPrice   = df_['high'][i]
                lowPrice    = df_['low'][i]
                volume      = df_['volume'][i]

                obj = stocks(
                            date        = date, 
                            stock       = stockName,
                            ticker      = ticker,
                            closePrice  = closePrice,
                            openPrice   = openPrice,
                            lowPrice    = lowPrice,
                            volume      = volume
                            )
                obj.save()
            
            total+=1

        except Exception as e:
            print("-------------ERROR----------------")
            print(e)
            try:
                print(df_)
            except:
                pass
            pass
            return
