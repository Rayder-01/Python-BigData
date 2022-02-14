import convertData as con
import requests
import json, csv
import pandas as pd
import os

# pd.option.mode.chained_assignment = None

filepath =  'stcokmonth01.csv'

if not os.path.isfile(filepath):
    url_twse = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20220101&stockNo=2330&_=1644050703773'
    res = requests.get(url_twse)
    jdata = json.loads(res.text)
    print(jdata) # 終端預覽取得的csv資料
    outputfile = open(filepath, 'w', newline='', encoding='utf-8-sig')
    outputwrite = csv.writer(outputfile) # 以 csv格式寫入檔案
    outputwrite.writerow(jdata['fields'])
    for dataline in (jdata['data']): # 寫入資訊
        outputwrite.writerow(dataline)
    outputfile.close() # 關閉檔案

pdstock = pd.read_csv(filepath, encoding='utf_8_sig') # 使用 pandas讀取csv檔案
for i in range(len(pdstock['日期'])):
    pdstock['日期'][i] = con.convertData(pdstock['日期'][i])
    print(pdstock['日期'][i])