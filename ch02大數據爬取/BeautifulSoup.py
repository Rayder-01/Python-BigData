from gettext import find
from pydoc import html
import requests
from bs4 import BeautifulSoup
# 網頁解析工具 BeautifulSoup
# 物件 = BeautifulSoup(原始碼, 'html.parser')

url = 'http://www.e-happy.com.tw'
html = requests.get(url)

sp = BeautifulSoup(html.text, 'html.parser')

# print(sp)