import requests
from bs4 import BeautifulSoup
import pandas
import re
import datetime
import pymysql

def createDF():
    global df
    year3 = []
    colspans = []
    dates = []
    days = []
    url = 'https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=6301000'
    res = requests.get(url)
    res.encodeing = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    trs = soup.find_all('tr') # 取得所有 tr 標籤

    year3.append("%d" % datetime.datetime.now().year)
    year3.append("%d" % (datetime.datetime.now() + 
      datetime.timedelta(days=1)).year)
    year3.append("%d" % (datetime.datetime.now() + 
      datetime.timedelta(days=2)).year)
    tdall = trs[0].findAll('th')
    k = 0
    for i in range(len(tdall)):
        th = tdall[i]
        if i > 0: # 從第二個 th開始
            if th.has_attr('colspan'): # BeautifulSoup has_attr('X') 取得'X'標籤
                colspans.append(th.attrs['colspan']) # 找到鍵值
            else:
                colspans.append("1")
            monthdate = re.findall('\d+', th.text) # 取得月日
            dates.append(year3[k] + '-' + monthdate[0] + 
              '-' + monthdate[1])
            days.append(re.findall('[一|二|三|四|五|六|日',
              th.text)[0]) # 取得星期.
            k+=1

    # 處理第2列
    ts = [] # 存日期和時間
    weekdays = [] #存星期幾
    hours = trs[1].findAll('span')
    k = 0
    for i in range(0, len(colspans)):
        for j in range(0, len(colspans[i])):  # 複製取值
            ts.append(dates[i] + '' +hours[k].text) # 日期 + 時間
            k += 1
            weekdays.append('星期' + days[i])
    df['日期時間'] = ts
    df['星期'] = weekdays

    #處理地3列
    wxs =[] # 儲存天氣狀況
    for img in trs[2].findAll('img'):
        wxs.append(img.attrs['alt']) # 文字資料位於alt屬性
    df['天氣狀況'] = wxs
    # 處理第9列以外的第4到10列
    vals = []
    for i in range(3, 10):
        if i is not 8: # 排除地9列
            tdall = trs[i].findAll('td')
            for j in range(len(tdall)):
                td = tdall[j]
                if j > 0: # 從第2列開始裁示資料
                    vals.append(td.text)
            df.iloc[:,i] = vals
            vals = []

createDF()    
print()