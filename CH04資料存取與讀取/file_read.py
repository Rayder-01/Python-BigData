from bcrypt import re
from matplotlib.pyplot import connect


f = open('file1.txt', 'r', encoding='UTF-8')

for line in f:
    print(line, end="")
f.close()

# 使用 with 來執行後關閉
# with open('file1.txt', 'r', encoding='UTF-8') as f:
#     for line in f:
#         print(line, end="")

# 認識 readlines() ,輸出成字串
with open('file1.txt', 'r', encoding='UTF-8') as f2:
    content =  f2.readlines()
    print(type(content))
    print(content)
