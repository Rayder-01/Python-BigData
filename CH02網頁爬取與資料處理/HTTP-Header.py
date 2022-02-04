from urllib import request
import requests
url = 'http://www.e-happy.com.tw'

#自訂header
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

#將header加入 GET 請求中
r = requests.get(url, headers = headers)
print(r)

#自訂header
# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
#     "Accept-Encoding": "gzip, deflate, br", 
#     "Accept-Language": "zh-TW,zh;q=0.9", 
#     "Host": "https://www.pexels.com/zh-tw/search/code/",  #目標網站 
#     "Sec-Fetch-Dest": "document", 
#     "Sec-Fetch-Mode": "navigate", 
#     "Sec-Fetch-Site": "none", 
#     "Upgrade-Insecure-Requests": "1", 
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36" #使用者代理
# }