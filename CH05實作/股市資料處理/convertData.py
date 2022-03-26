# 從 台灣證券交易所 取得 XHR
# 檢查 -> network -> headers -> STOCK_DAY?
#https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20220101&stockNo=2330&_=1644050703773

# 自訂 日期格式轉換函示
def convertData(date):
    strl = str(date)
    yearstr = strl[:3]
    realyear = str(int(yearstr)+1911)
    realdate = realyear + strl[4:6] + strl[7:9]
    return realdate

print(convertData('110/01/02')) 