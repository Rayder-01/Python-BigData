# http://www.cwb.gov.tw/v7/forecast/town368/3Hr/鄉鎮市區代碼.htm
# https://www.cwb.gov.tw/V8/C/
# https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=6301000
import pandas

df = pandas.read_excel('CH05實作\建立天氣預報API\村里代碼對照表.xlsx') # 使用檔案 相對路近較佳
header = df.iloc[2] 
df1 = df[3:].copy()
df2 = df1.rename(columns=header)
df3 = df2.drop(columns=['縣市代碼','村里代碼','村里名稱','村里代碼'])
df4 = df3.drop_duplicates()
df4.to_csv('村里代碼(已處理資料).csv', encoding='big5', index=False)
print(header)
print(df1)
print(df2)
print(df3)
print(df4)