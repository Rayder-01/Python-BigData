import requests
from bs4 import BeautifulSoup

# 認識get post 取得 PTT 論壇的 資料
payload = {
    'from': 'https://www.ptt.cc/bbs/Gossoping/index.html',
    'yes': 'yes'
}

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

rs = requests.Session()
rs.post('https://www.ptt.cc/ask/over18', data=payload,
           headers = headers)

res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html',
              headers = headers)

soup = BeautifulSoup(res.text, 'html.parser')
items = soup.select('.r-ent')

for item in items:
    print(item.select('.date')[0].text,
          item.select('.author')[0].text,
          item.select('.title')[0].text)