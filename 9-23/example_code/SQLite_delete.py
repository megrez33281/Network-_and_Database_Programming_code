import sqlite3 

conn=sqlite3.connect ('C:\\Users\\Liu\\Desktop\\2024 Python\\4. SQLite\\Programmer.db')
cur=conn.cursor()
cur.execute("select * from Programmer")
rows = cur.fetchall()
for row in rows:
    print(row)
print ("--------------------------------------")    
cur.execute ("delete from Programmer where Name='Diana'")
cur.execute("select * from Programmer")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()