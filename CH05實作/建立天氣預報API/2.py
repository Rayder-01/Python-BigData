import requests
from bs4 import BeautifulSoup
import pandas
import re
import datetime
import pymysql
from selenium import webdriver
def createDF():
    global df
    year3 = []
    colspans = []
    dates = []
    days = []
    # Driver
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
    driver.maximize_window()

    url = 'https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=6301000'
    driver.get(url)
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(driver.page_source, 'html5lib')
    
    trs1 = soup.find("div",{"id":"PC_week"})
    trs = trs1.find_all('tr')
    # print(trs)


    year3.append("%d" % datetime.datetime.now().year)
    year3.append("%d" % (datetime.datetime.now() + 
      datetime.timedelta(days=1)).year)
    year3.append("%d" % (datetime.datetime.now() + 
      datetime.timedelta(days=2)).year)
    tdall = trs[0].findAll('th')
    # print(tdall[0])


    k = 0
    for i in range(len(tdall)):
        td = tdall[i]
        if i > 0: # 從第二個 th開始
            if td.has_attr('colspan'): # BeautifulSoup has_attr('X') 取得'X'標籤
                colspans.append(td.attrs['colspan']) # 找到鍵值
            else:
                colspans.append("1")
            monthdate = re.findall('\d+', td.text) # 取得月日
            dates.append(year3[k] + '-' + monthdate[0] + 
              '-' + monthdate[1])
            days.append(re.findall('[一|二|三|四|五|六|日]',
              td.text)[0]) # 取得星期.
            k+=1
        print(days)

    # 處理第2列
    ts = [] # 存日期和時間
    weekdays = [] #存星期幾
    hours = trs[1].findAll('span')
    k = 0
    for i in range(0, len(colspans)):
        for j in range(0, int(colspans[i])):  # 複製取值
            ts.append(dates[i] + ' ' +hours[k].text) # 日期 + 時間
            k += 1
            weekdays.append('星期' + days[i])
    df['日期時間'] = ts
    df['星期'] = weekdays
    print(df)
    #處理地3列
    wxs =[] # 儲存天氣狀況
    for img in trs[2].findAll('img'):
        wxs.append(img.attrs['alt']) # 文字資料位於alt屬性
    df['天氣狀況'] = wxs
    print(df)
    # 處理第9列以外的第4到10列
    vals = []

    for i in range(3, 10):
        B = 5
        A = 8
        if i != B and i != A: # 排除地5列 降雨機率
            tdall = trs[i].findAll('td')
            # print(tdall)
            for j in range(len(tdall)):
                # print(i,":",j,":",len(tdall))
                if j != 8:
                    td = tdall[j]
                    vals.append(td.text)
                # print(vals)
            df.iloc[:,i] = vals
            print(df.iloc[:,i])
            vals = []


    print(df)
    # print(vals)
    # # 處理第5列
    # pops = [] # 儲存降雨機率
    # rep = 0 # 重複次數
    # tdall = trs[5].findAll('td')
    # for i in range(len(tdall)):
    #     td = tdall[i]
    #     if i > 0:
    #         if td.has_attr('colspan'): # 如果 colspan存在
    #             rep = int(td.attrs['colspan']) # colspan 屬性值就是重複次數
    #         else:
    #             rep = 1 # 若沒 colspan就不重複取值
    #         for j in range(0, rep): # 重複取值
    #             pops.append(td.text)
    # df['降雨機率'] = pops
    print(df)
# def writeMySql():
#     global df
#     try:
#         conn = pymysql.connect('localhost',port=3306,user='root',
#           passwd='1234',charset='utf8', db='weather') # 連結資料庫
#         cursor = conn.cursor()
#     except:
#         print('資料庫連結錯誤')
#         return

columns = ['日期時間','星期','天氣狀況','溫度','體感溫度','降雨機率',
           '相對濕度','蒲福風級','風向','舒適度']   
df = pandas.DataFrame(columns=columns) # 建立DataFrame
createDF()    
# print()