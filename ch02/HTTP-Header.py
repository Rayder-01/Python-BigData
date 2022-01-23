
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