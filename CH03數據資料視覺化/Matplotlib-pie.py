import matplotlib.pyplot as plt


# 中文設定
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

labels = ["東部", "南部", "北部", "中部"]
data = [5, 10, 20 ,15] 
colors = ["red", "green", "blue", "yellow"]

explode = (0, 0, 0.05, 0)

plt.pie(data, explode=explode, labels=labels, colors=colors,\
     labeldistance=1.1, autopct="%3.1F%%", shadow=False,\
     startangle=90, pctdistance=0.6)
plt.axis("equal")

plt.legend()
plt.show()