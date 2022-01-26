import matplotlib.pyplot as plt

# 中文設定
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

listx = [1,5,7,9,13,16]
listy = [15,50,80,40,70,50]

# 線型圖
plt.plot(listx, listy,label="線型圖", color='r') # color="red", lw="5.0", is="--", lebel="food"
# 長條圖
plt.bar(listx, listy,label="長條圖")

plt.title("title")
plt.xlabel("xlabel")
plt.ylabel("ylabel")

# 設定座標範圍
# plt.xlim(0, 100)
# plt.ylim(0, 100)

plt.legend()
plt.show()