import twstock

# 用twstock來查詢股市資訊
stock = twstock.Stock('2317')
print('近一個月的收盤價')
print(stock.price)
print('近6個收盤價:')
print(stock.price[-6:])

real = twstock.realtime.get('2317')
if real['success']:
    print('及時股票資料:')
    print(real) # 即時資料
else:
    print('錯誤:' +real['rtmessage'])

print('目前股價')
print(real['realtime']['latest_trade_price']) # 及時價格