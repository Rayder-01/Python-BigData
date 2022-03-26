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

    url = 'https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=1000901'
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


    #處理地3列
    wxs =[] # 儲存天氣狀況
    for img in trs[2].findAll('img'):
        wxs.append(img.attrs['alt']) # 文字資料位於alt屬性
    df['天氣狀況'] = wxs

 

    # 處理第6到8列
    vals = []
    for i in range(6, 8):
        tdall = trs[i].findAll('td')
        for j in range(len(tdall)):
            td = tdall[j]
            vals.append(td.text)

        df.iloc[:,i] = vals
        vals = []
    # 處理第4到5列
    for i in range(3, 5):  
        tdall = trs[i].findAll('td')
        # tdall = tdall.find_all('span')
        for j in range(len(tdall)):
            td = tdall[j]
            vals.append(td.text[:2])
        df.iloc[:,i] = vals
        vals = []
    # 處理第9列
    tdall = trs[9].findAll('td')
    for i in range(len(tdall)):
        td = tdall[j]
        vals.append(td.text)
    df.iloc[:,8] = vals
    vals = []

    # 處理第10列
    tdall = trs[10].findAll('td')
    for i in range(len(tdall)):
        td = tdall[j]
        vals.append(td.text)
    df.iloc[:,9] = vals

    # 處理第5列
    pops = [] # 儲存降雨機率
    rep = 0 # 重複次數
    tdall = trs[5].findAll('td')
    for i in range(len(tdall)):
        td = tdall[i]

        if td.has_attr('colspan'): # 如果 colspan存在
            rep = int(td.attrs['colspan']) # colspan 屬性值就是重複次數
        else:
            rep = 1 # 若沒 colspan就不重複取值
        for j in range(0, rep): # 重複取值
                pops.append(td.text)
    df['降雨機率'] = pops
    print(df)


def writeMySql():
    global df
    db_settings = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "",
        "db": "weather",
    }
    try:
        conn = pymysql.connect(**db_settings) # 將 資料設定 做成 conn物件
        cursor = conn.cursor() # 使用cursor()方法獲取操作 物件
    except:
        print('資料庫連結錯誤')
        return
    # 如果 threeday 資料表不存在就建立該資料表
    try:
        sql = "SELECT * FROM threeday LIMIT 1;"
        cursor.execute(sql)
    except:
        sql = """
        CREATE TABLE if not exists threeday (
        rid int not null auto_increment primary key,
        日期時間 timestamp,
        星期 char(30),
        天氣狀況 char(32),
        溫度 int,
        體感溫度 int,
        降雨機率 char(4),
        相對濕度 char(4),
        蒲福風級 char(15),
        風向 char(3),
        舒適度 char(8)
        )
        """
        cursor.execute(sql)
    for i in df.index: # 逐行處理 dataframe
        exist = cursor.execute("select * from threeday where \
          日期時間='" + df.loc[i][0] +  "'") # select 日期時間
        if exist == 0:
            cursor.execute('insert into threeday(日期時間,星期,天氣狀況, \
            溫度,體感溫度,降雨機率,相對濕度,蒲福風級,風向,舒適度)\
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            tuple(df.loc[i])) # 將資料加入資料表
    
    conn.commit()
    cursor.close()
    conn.close()
    print('資料庫threeday資料表處理完畢')


columns = ['日期時間','星期','天氣狀況','溫度','體感溫度','降雨機率',
           '相對濕度','蒲福風級','風向','舒適度']   
df = pandas.DataFrame(columns=columns) # 建立DataFrame

createDF()
writeMySql()
# print()