import matplotlib.pyplot as plt
import convertData as con
import requests
import json, csv
import pandas as pd
import os

# pd.option.mode.chained_assignment = None

#中文設定
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

filepath =  'stcokmonth01.csv'

if not os.path.isfile(filepath):
    url_twse = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20220101&stockNo=2451&_=1644050703773'
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
print(pdstock['日期'])
for i in range(len(pdstock['日期'])):
    pdstock['日期'][i] = con.convertData(pdstock['日期'][i])
    print(pdstock['日期'][i])
pdstock['日期'] = pd.to_datetime(pdstock['日期']) # 轉換日期欄位為日期格式
print(pdstock)
x = pdstock['日期']
y1 = pdstock['收盤價']
y2 = pdstock['最低價']
y3 = pdstock['最高價']
plt.plot(x, y1, label='收盤價')
plt.plot(x, y2, label='最低價')
plt.plot(x, y3, label='最高價')
plt.legend()
plt.show()
# pdstock.plot(kind='line', figsize=(12, 6), x='日期', y=['收盤價','最低價','最高價'])

