import sqlite3 

conn=sqlite3.connect ('C:\\Users\\Liu\\Desktop\\2024 Python\\4. SQLite\\Programmer.db')
cur=conn.cursor()
cur.execute ("select * from Programmer")

#rows = cur.fetchall()
#for row in rows:
#    print(row)
row=cur.fetchone()
print(row)
row=cur.fetchone()
print(row)

conn.commit()
conn.close()