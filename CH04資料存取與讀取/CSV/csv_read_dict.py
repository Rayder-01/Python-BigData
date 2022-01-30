import csv
with open('csv_dict.csv', newline='') as csvfile:
    # 讀取 csv 檔內容，將每一列轉成 dictionary
    rows = csv.DictReader(csvfile)
    for row in rows:
        print(row['姓名'],row['身高'],row['體重'])