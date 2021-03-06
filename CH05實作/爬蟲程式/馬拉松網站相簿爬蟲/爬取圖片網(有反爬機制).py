import time,os
from urllib.request import urlopen
from selenium import webdriver
from bs4 import BeautifulSoup

# 使用 google chromedriver:
# https://sites.google.com/a/chromium.org/chromedriver/download
# 下載 chromedriver_win32.zip
# 解決 chromedriver.exe 容易出現的 path 問題
# 放置在C:\Program Files (x86)\Google\Chrome\Application\ 目錄裡 將path設為絕對路進

# https://www.pexels.com/zh-tw/search/code/ 有防爬
# http://tw.running.biji.co?index.php?q=album&act=photo_list&album_id=30668&cid=5791&type=album&subtitle
# https://running.biji.co/index.php?q=album&act=photo_list&album_id=30668&cid=5791&type=place&subtitle=%E7%AC%AC3%E5%B1%86%E5%9F%94%E9%87%8C%E8%B7%91+Puli+Power+%E5%B1%B1%E5%9F%8E%E6%B4%BE%E5%B0%8D%E9%A6%AC%E6%8B%89%E6%9D%BE-%E5%90%91%E5%96%84%E6%A9%8B(%E7%B4%8434K)%20(3,900)
# 建立一個後續可以使用在操作瀏覽器的物件

options = webdriver.ChromeOptions()
# 设置中文
options.add_argument('lang=zh_CN.UTF-8')
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"
# 
options.add_argument('user-agent=%s' % user_agent)

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver',chrome_options=options)
driver.maximize_window()
url = 'https://www.pexels.com/zh-tw/search/code/'

driver.get(url)
# 等待1秒
driver.implicitly_wait(1)
print("圖片下載中")
for i in range(1,10):
    driver.execute_script("window.scrollTo(0,\
      document.body.scrollHeight);")
    time.sleep(0.3)

soup = BeautifulSoup(driver.page_source,'html.parser')
all_img = soup.find_all('img',{"class":"photo-item__img"})

# 以該網站標題建立資料夾
title = '相簿' + "/"
img_dir = title
print(img_dir)
if not os.path.exists(img_dir):
    os.mkdir(img_dir)

# 處理 <img> 標籤
n = 0
for img in all_img:
    # 讀取 src 屬性內容
    src = img.get('src')
    # print(src)
    # 讀取 .jpg 檔
    if src != None :
        # 設定圖檔路徑
        full_path = src
        filename = full_path.split('?')[0] #取的檔名
        # print(filename)
        # 儲存圖片
        try:
            image = urlopen(full_path)
            with open(os.path.join(img_dir,filename),'wb') as f:

                f.write(image.read())
                f.close()
            n +=1
            if n>= 2: # 最多下載張數
                break
        except:
            print("{} 無法讀取!".format(filename))


        # try:
            # image = urlopen(full_path)
            # with open(os.path(img_dir),'wb') as f:
            #     f.write(image.read())
            # n +=1
            # if n>= 2: # 最多下載張數
            #     break
        # except:
        #     print("{} 無法讀取!".format(filename))

print("共下載",n,"張圖片")
driver.quit();