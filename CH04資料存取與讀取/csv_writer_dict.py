import csv

from nbformat import write

with open('csv_dict.csv', 'w', newline='') as csvfile:
    
    filenames = ['姓名','身高','體重']
    # 使用 dictionary 來寫入 csv
    writer = csv.DictWriter(csvfile, fieldnames=filenames)
    # 寫入 欄位名稱
    writer.writeheader()
    writer.writerow({'姓名':'Tom', '身高':'170', '體重':60})
    writer.writerow({'姓名':'Momo', '身高':'180', '體重':80})
