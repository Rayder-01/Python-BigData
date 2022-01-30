import csv

with open('csv_write.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['姓名', '身高', '體重'])
    writer.writerow(['Tom', 170, 65])
    writer.writerow(['Tumy', 185, 88])
    