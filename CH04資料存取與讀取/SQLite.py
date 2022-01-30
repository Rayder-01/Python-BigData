import sqlite3

conn = sqlite3.connect('test.sqlite')
cursor = conn.cursor()

# SQL CREATE
sqcreate = 'CREATE TABLE IF NOT EXISTS table01 \
("num" INTEGE PRIMARY KEY NOT NULL , "tel" TEXT)'
cursor.execute(sqcreate)

# INSERT INTO
sqcreate = 'insert into table01 values(1, "02-12345678")'
cursor.execute(sqcreate)

conn.commit() # 主動更新
conn.close() # 關閉資料庫連線
