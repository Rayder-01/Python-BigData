from turtle import title
import matplotlib.pyplot as plt
import pandas as pd

# 中文設定
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

datas = [[65,92,78,83,70],
         [90,72,76,93,56],
         [81,85,91,89,77],
         [79,53,47,94,80]]

columns = ["國文","數學","英文","自然","社會"]
indexs = ["Tom","Mins","Charty","Miky"]

df = pd.DataFrame(datas, columns=columns, index=indexs)
df.plot(kind='barh', title='學生成績', fontsize=8)
plt.show()
