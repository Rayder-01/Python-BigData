from CH05實作.民國西元轉換 import convertData
import convertData

import requests
import json, csv
import pandas as pd
import os

# pd.option.mode.chained_assignment = None

filepath =  'stcokmonth01.csv'

if not os.path.isfile(filepath):
    url_twse = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20220101&stockNo=2330&_=1644050703773'
    res = requests.get(url_twse)

