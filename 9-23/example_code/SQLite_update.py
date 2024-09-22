import sqlite3 

conn=sqlite3.connect ('C:\\Users\\Liu\\Desktop\\2023 Python\\5. SQLite\\Programmer.db')
cur=conn.cursor()
cur.execute("select * from Programmer")
rows = cur.fetchall()
for row in rows:
    print(row)
print ("--------------------------------------")    
cur.execute ("update Programmer set Name= 'Brian' where ID=2")
cur.execute("select * from Programmer")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()