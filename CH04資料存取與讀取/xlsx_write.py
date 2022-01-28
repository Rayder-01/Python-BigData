import openpyxl

# 創建工作簿
workbook = openpyxl.Workbook()

# 取得第一個工作表
sheet1 = workbook.worksheets[0]

sheet1['A1'] = 'A1'
sheet1['B1'] = 'B1'
listtile = ["姓名", "電話"]
sheet1.append(listtile)
listdata = ["Tom","096666666"]
sheet1.append(listdata)

workbook.save('test.xlsx')