import requests
from bs4 import BeautifulSoup
# 網頁解析工具 BeautifulSoup
# 物件 = BeautifulSoup(原始碼, 'html.parser')

url = 'http://www.e-happy.com.tw'
html = requests.get(url)
#  requests.encoding 選擇編碼 解決亂碼問題
html.encoding = "hbk"
sp = BeautifulSoup(html.text, 'html.parser')
# sp.find_all("a")
tit = sp.select("title")

print(tit)
# apparent_encoding
