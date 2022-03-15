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
    tdall = trs[0].findAll('td')
    k = 0
    for i in range(len(tdall)):
        th = tdall[i]
        if i > 0: # 從第二個 th開始
            if th.has_attr('colspan'): # BeautifulSoup has_attr('X') 取得'X'標籤
                colspans.append(th.attrs['colspan']) # 找到鍵值
            else:
                colspans.append("1")
            monthdate = re.findall('\d+', td.text) # 取得月日
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
        if i != 5 | 8: # 排除地5列 降雨機率
            print('成功')
            tdall = trs[i].findAll('td')
            print('成功')
            for j in range(len(tdall)):
                td = tdall[j]
                if j > 0: # 從第2列開始裁示資料
                    vals.append(td.text)
            df.iloc[:,i] = vals
            vals = []
    # 處理第5列
    pops = [] # 儲存降雨機率
    rep = 0 # 重複次數
    tdall = trs[4].findAll('td')
    for i in range(len(tdall)):
        td = tdall[i]
        if i > 0:
            if td.has_attr('colspan'): # 如果 colspan存在
                rep = int(td.attrs['colspan']) # colspan 屬性值就是重複次數
            else:
                rep = 1 # 若沒 colspan就不重複取值
            for j in range(0, rep): # 重複取值
                pops.append(td.text)
    df['降雨機率'] = pops

def writeMySql():
    global df
    try:
        conn = pymysql.connect('localhost',port=3306,user='root',
          passwd='1234',charset='utf8', db='weather') # 連結資料庫
        cursor = conn.cursor()
    except:
        print('資料庫連結錯誤')
        return

columns = ['日期時間','星期','天氣狀況','溫度','體感溫度','降雨機率',
           '相對濕度','蒲福風級','風向','舒適度']   
df = pandas.DataFrame(columns=columns) # 建立DataFrame
createDF()    
print()