import matplotlib.pyplot as plt
import yearurl
import requests
import json, csv
import pandas as pd
import os
import time

def convertData(date):
    strl = str(date)
    yearstr = strl[:3]
    realyear = str(int(yearstr)+1911)
    realdate = realyear + strl[4:6] + strl[7:9]
    return realdate
# pd.option.mode.chained_assignment = None
# 完整網址 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20220101&stockNo=2451&_=1644050703773'
urlbase = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2021' # 網址前半段
urltail = '01&stockNo=2451&_=1644050703773'

filepath =  'stcokyear2022.csv'

if not os.path.isfile(filepath):
    for i in range(1,13):
        url_twse = urlbase + yearurl.twodgit(i) + urltail
        res = requests.get(url_twse)
        jdata = json.loads(res.text)

        #print(jdata) # 終端預覽取得的csv資料
        outputfile = open(filepath, 'a', newline='', encoding='utf-8-sig')
        outputwrite = csv.writer(outputfile) # 以 csv格式寫入檔案
        if i==1:
            outputwrite.writerow(jdata['fields'])     
        for dataline in (jdata['data']): # 寫入資訊
            outputwrite.writerow(dataline)
        time.sleep(0.5)
    outputfile.close() # 關閉檔案

pdstock = pd.read_csv(filepath, encoding='utf_8_sig') # 使用 pandas讀取csv檔案
print(pdstock)
