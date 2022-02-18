# 從 台灣證券交易所 取得 XHR
# 檢查 -> network -> headers -> STOCK_DAY?
#https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20220101&stockNo=2330&_=1644050703773
#https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20220211&stockNo=2451&_=1644584776497

# 了解 台灣證券交易所 提供的單日股票價格url格式
# 試著更改格式取得需要的月份日期

def twodgit(n):
    if(n < 10):
        retstr = '0' + str(n)
    else:
        retstr = str(n)
    return retstr

urlbase = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2021'
urltail = '01&stockNo=2451&_=1644584776497'

for i in range(1, 13):
    url_twse = urlbase + twodgit(i) + urltail
    print(url_twse)
#