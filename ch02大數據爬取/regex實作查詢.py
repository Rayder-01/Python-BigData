html = '''
<div class = "content">
    E-Mail:<a href = "mailto:mail@test.com.tw">mail</a><br>
    E-Mail2:<a href="mailto:mail2@test.com.tw">mail2</a><br>
    <ul class="price">定價:360元</ul>
    <img src = "http://test.com.tw/p1.jpg">
    <img src = "http://test.com.tw/p2.jpg">
    <img src = "http://test.com.tw/p3.jpg">
</div>
'''

# 實際從 HTML中找出 定價 jpg 和 電子郵件

import re
from bs4 import BeautifulSoup

sp = BeautifulSoup(html,'html.parser') # (原始碼,解析原始碼)

#搜尋所有電子郵件
emails = re.findall(r'[a-zA-z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-z0-9-.]+',html)

for email in emails:
    print(email)

# 搜尋價格
price = re.findall(r"[\d]+",sp.select('.price')[0].text)[0]
print(price)
# 搜尋jpg圖檔
regex = re.compile('.*\.jpg')
imglist = sp.find_all("img",{"src":regex})
for a in imglist:
    print(a["src"])