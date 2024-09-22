#download SQLite browser at https://sqlitebrowser.org/dl/ and open mydb.db to browse the data base
import sqlite3 

conn=sqlite3.connect ('C:\\Users\Liu\Desktop\mydb.db')
#使用此指令創建資料後，在檔案中尋找mydb.db檔案，並可用SQLite browser瀏覽
# conn=sqlite3.connect ('E:\\Course\\Network programming\\2022 Python\\5. SQLite\\mydb.db') 
cur=conn.cursor()
cur.execute ("create table USER2 (ID, NAME)")
conn.commit()
conn.close()






