import re

# 使用 ASCII編碼 re moduel 裡面的正規表示式 regular expression (regex) 來處理找尋字串
# http://pythex.org/ 實用的測試網站

# 認識 正規表示運算子
# + 代表可以重複多個 112233
# . 除了\n以外的所有字元 a.c = a1c
# ^ 代表輸入的開始 ^ab -> a1c23 = None
# $ 輸入列的結束 23$ -> a1c23 =  23
# * 代表前一個項目可以出現0次或多次 ac* -> acc123 = acc

m1 = re.match(r'[a-z]+','tem123po') # 找到 a-z 直到不符合就停止
m2 = re.search(r'[a-z]+','3tem12po') # 找到第一組符合字串 並回傳 match
m3 = re.findall(r'[a-z]+','3tem12po') # 找到所有符合字串
reobj = re.compile(r'[a-z]+')
m4 = reobj.findall('3tem12po')
print(m1)
# 物件的方法
# print(m1.group())  tem
# print(m1.start())  0
# print(m1.end())    3
# print(m1.span())   0,3

print('search:',m2)

print('findall:',m3)
print('compile + findall:',m3)