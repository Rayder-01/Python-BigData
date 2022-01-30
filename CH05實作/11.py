from lib2to3.pgen2 import driver
import time,os
from urllib.request import urlopen
from selenium import webdriver
from bs4 import BeautifulSoup
# 使用 google chromedriver:
# https://sites.google.com/a/chromium.org/chromedriver/download
# 下載 chromedriver_win32.zip
# 解決 chromedriver.exe 容易出現的 path 問題
# 放置在C:\Program Files (x86)\Google\Chrome\Application\ 目錄裡 將path設為絕對路進

# 建立一個後續可以使用在操作瀏覽器的物件
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')

driver.maximize_window()

url = 'https://www.pexels.com/zh-tw/search/code/'

driver.get(url)