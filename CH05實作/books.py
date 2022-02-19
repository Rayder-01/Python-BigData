from matplotlib.pyplot import title


def showbook(url,kind):
    html = request.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    try:
        pages = int(soup.select('.nct_page span')[0].text) # 計算頁數
        print("共有",pages,"頁")
        for page in range(1,pages+1):
            pageurl = url + '&page=' + str(page).strip()
            print("第",page,"頁",pageurl)
            showpage(pageurl,kind)
    except: # 沒有分頁處理
        showpage(url, kind)

def showpage(url, kind):
    html = request.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    # 近期新書、在 class = "mod_b type02_l001-1 clearfix"
    res = soup.find_all('div',{'class':"mod_b type02_l001-1 clearfix"})[0]
    items = res.select('.item') # 所有 item
    n = 0 # 計算分頁書本數目
    for item in items:
        msg = item.select('.msg')[0]
        scr = item.select('a img')[0]["src"]
        title = msg.select('a')[0].text
        imgurl = scr.split("?i=")[-1].split("&")[0] #ex:https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/091/65/0010916571.jpg&v=6200f4bc&w=170&h=170
        author = msg.

# https://www.books.com.tw/web/books_nbtopm_19/?v=1&o=5