import sqlite3 as lite

con = lite.connect('C:\\Users\\Liu\\Desktop\\2024 Python\\4. SQLite\\Programmer.db')

with con:
    cur=con.cursor()
    cur.execute("Insert into Programmer Values(1, 'Diana', 'Python')")
    cur.execute("Insert into Programmer Values(2, 'Tony', 'C')")
    con.commit()
    
con.close()