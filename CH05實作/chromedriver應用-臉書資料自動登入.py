# pip install selenium 模組
# https://sites.google.com/a/chromium.org/chromedriver/download
# 下載 chromedriver_win32.zip

# 自動填入資料 應用

from selenium import webdriver
driver = webdriver.Chrome('CH05實作\chromedriver.exe')

url = 'https://zh-tw.facebook.com/'
email = '填入'
password = '填入'

driver.maximize_window()
driver.get(url)

# find_element_by_[對應填入HTML欄位內的屬性]
driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_name('login').click()

#driver.quit()