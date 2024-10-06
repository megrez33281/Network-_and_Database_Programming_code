# install MySQL 
# see instalation guide https://www.itread01.com/articles/1476681060.html 
# download mySQL community server at https://dev.mysql.com/downloads/mysql/
# Install MySQL workbench
# install "mysqlclient" by running "pip install --only -binary :all: mysqlclient" 
# see https://stackoverflow.com/questions/29846087/microsoft-visual-c-14-0-is-required-unable-to-find-vcvarsall-bat

import MySQLdb
db=MySQLdb.connect(host="localhost", user="newuser", password="Test1234", db="test_db")
cur=db.cursor()
cur.execute("Select * from employee" )
for emp in cur.fetchall():
    print(emp)
print ("-----------------------------------------------------")    
cur.execute("insert into Employee values(13, 'Stranger', 33000)" )

# 該資料庫 (schema)的權限必須開放select (custom)給該user
cur.execute("Select * from employee" )
for emp in cur.fetchall():
    print(emp)

db.commit()
db.close()