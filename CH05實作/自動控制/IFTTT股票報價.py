import twstock
import time
import requests

counterLine = 0
counterError = 0

print('開始執行')
while True:
    realdata = twstock.realtime.get('2324') # 即時資料
    if realdata['success']:
        realprice = realdata['realtime']['latest_trade_price'] # 目前股價
        if float(realprice) >=21:
            print('仁寶目前股價:'+ realprice)
            counterLine = counterLine+1
            # https://ifttt.com/connect/{connection_id}?email={your-email@address.com}
            # https://maker.ifttt.com/trigger/Stock_price_Service/with/key/dTLdIQWvYiQD_kgyx2LcUr?value1=1 測試用網址
            url_ifttt = 'https://maker.ifttt.com/trigger/Stock_price_Service/with/key/dTLdIQWvYiQD_kgyx2LcUr?value1='+realprice # 發送價格
            real = requests.get(url_ifttt)
            print('第'+str(counterLine)+'次發送LINE回傳訊息:'+real.text)
        if counterLine >= 3: # 發送三次就結束程式
            print('程式結束')
            break
        for i in range(1):
            time.sleep(1) # 每 5分鐘讀一次
    else:
        print('twstock 讀取錯誤,錯誤原因:'+realdata['rtmessage'])
        counterError = counterError + 1
        if counterError >= 3:
            print('程式結束')
            break
        for i in range(300):
            time.sleep(300)

