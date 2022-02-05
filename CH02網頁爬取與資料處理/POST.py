import requests

payload = {'Key1': 'value1','key2':'value2'}

#將查詢參數加入 POST 請求中
html = requests.post("http://httpbin.org/post", data=payload)
print(html.text)
print(html.url)

# GET請求是用來向伺服器傳送索取資料的一種請求，實際應用中資料不涉及到安全性，可用GET方式來向後端請求資料，
# 如分頁或搜尋關鍵詞 "http://www.xxx.com/product?keywords=xxx&page=2";

# POST請求是向伺服器提交資料的一種請求，涉及到安全性的資料，用POST的方式來傳輸較GET更安全。