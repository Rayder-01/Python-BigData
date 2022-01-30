import pymysql

# 資料庫設定
db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "",
    "db": "bigdatadb",
}

conn = pymysql.connect(**db_settings) # 將 資料設定 做成 conn物件

# 使用cursor()方法獲取操作 物件
cursor = conn.cursor()

# 如果資料表已經存在使用 execute() 方法刪除表。
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 建立資料表SQL語句
sqlC = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
         
sqlI ="""INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

sqlS ="SELECT * FROM EMPLOYEE"
try:
    cursor.execute(sqlC) 
    # 提交到資料庫執行
    conn.commit()
except:
    # Rollback in case there is any error
    conn.rollback()

try:
    cursor.execute(sqlI)
    # 提交到資料庫執行
    conn.commit()
except:
    # Rollback in case there is any error
    conn.rollback()

try:
   # Execute the SQL command
   cursor.execute(sqlS)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      #print (row)
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # Now print fetched result
      print ("name = %s %s,age = %s,sex = %s,income = %s" % \
             (fname, lname, age, sex, income ))
except:
   import traceback
   traceback.print_exc()
   print ("Error: unable to fetch data")

# 關閉資料庫連線
conn.close()
