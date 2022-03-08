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
              th.text)[0]) # 取得星期
print(createDF)

    