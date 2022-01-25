import pandas as pd

# 使用 pandas 整理資料 輸出資料

datas = [[65,92,78,83,70],
         [90,72,76,93,56],
         [81,85,91,89,77],
         [79,53,47,94,80]]

colums = ["國文","數學","英文","自然","社會"]
indexs = ["Tom","Mins","Charty","Miky"]

df = pd.DataFrame(datas, columns=colums, index=indexs)
print(df)

# 認識 class 內的 to_xxx 方法
df.to_csv('out.csv', encoding="utf-8-sig")

# df.to_excel
# df.to_sql
# df.to_json
# df.to_html