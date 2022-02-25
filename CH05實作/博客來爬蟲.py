def showbook(url,kind):
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    try:
        pages = int(soup.select('.cnt_page span')[0].text) # 計算頁數
        print("共有",pages,"頁")
        for page in range(1,pages+1):
            pageurl = url + '&page=' + str(page).strip()
            print("第",page,"頁",pageurl)
            showpage(pageurl,kind)
    except: # 沒有分頁處理
        showpage(url, kind)

def showpage(url, kind):
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    # 近期新書、在 class = "mod_b type02_l001-1 clearfix"
    res = soup.find_all('div',{'class':"mod type02_m012 clearfix"})[0]
    items = res.select('.item') # 所有 item
    n = 0 # 計算分頁書本數目
    for item in items:
        msg = item.select('.msg')[0]
        scr = item.select('a img')[0]["src"]
        title = msg.select('a')[0].text
        imgurl = scr.split("?i=")[-1].split("&")[0] #ex:https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/091/65/0010916571.jpg&v=6200f4bc&w=170&h=170
        author = msg.select('a')[1].text
        publish = msg.select('a')[2].text
        date = msg.find('span').text.split(':')[-1]
        onsale = item.select('.price .set2')[0].text
        content = item.select('.txt_cont')[0].text.replace(" ","").strip()
        # 將資料加入 list1
        listdata = [kind,title,imgurl,author,publish,date,onsale,content]
        list1.append(listdata)
        print("\n分類"+kind)
        print("書名:"+title)
        print("圖片網址:"+imgurl)
        print("作者:"+author)
        print("出版社:"+publish)
        print("出版日期:"+date)
        print(onsale)
        print("內容:"+content)
        n+=1
        print("n=",n)
        if n==10:break #開發用

def twobyte(kindno):
    if kindno<10:
        kindnostr="0"+str(kindno)
    else:
        kindnostr = str(kindno)
    return kindnostr

import requests
from bs4 import BeautifulSoup
import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.worksheets[0]
list1=[]

kindno = 19 # 網址書籍總類分類用
homeurl = 'https://www.books.com.tw/web/books_nbtopm_19/?v=1&o=5'
html = requests.get(homeurl).text

# 爬取所有種類用
mode = "?v=1&o=5"
url = "https://www.books.com.tw/web/books_nbtopm_"

soup = BeautifulSoup(html, 'html.parser')
# 中文書新書分類，總類別數量
res = soup.find('div',{'mod_b type02_l001-1 clearfix'})
hrefs = res.select("a")
for href in hrefs:
    kindurl = url + twobyte(kindno) + mode # 分類網址段落 # 爬取所有種類用
    print("\nkindno=",kindno)
    kind = href.text # 分類
    showbook(kindurl,kind)
    kindno += 1
    if kindno ==20:break # 只選一種書籍種類 使用

# excel
listtitle=["分類","書名","圖片網址","作者","出版社","出版日期","優惠價","內容"]
sheet.append(listtitle)
for item1 in list1:
    sheet.append(item1)

workbook.save('books_all.xlsx')

# https://www.books.com.tw/web/books_nbtopm_19/?v=1&o=5