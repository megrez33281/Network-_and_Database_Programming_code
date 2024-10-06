import MySQLdb


def OperateDataBase(command):
    db = MySQLdb.connect(host="localhost", user="apple", password="911004", db="test")
    cur=db.cursor()
    cur.execute(command)
    db.commit()
    db.close()

def QueryOperate(command):
    db = MySQLdb.connect(host="localhost", user="apple", password="911004", db="test")
    cur=db.cursor()
    cur.execute(command)
    contents = cur.fetchall()
    db.commit()
    db.close()
    return contents

def MakeCommand(content):
    command = ""
    if type(content) == str:
        command = "'" + content + "'"
    else:
        command = str(content)
    return command

def InsertData(dest,  content_list):

    command = "insert into " + dest + " values("
    for i in range(0, len(content_list)):

        content = MakeCommand(content_list[i])
        if i != len(content_list)-1:
            command += content + ", "
        else:
            command +=  content + ")"

    print(command)
    OperateDataBase(command)

def UpdateData(dest, col_list,  value_list, condition = ""):
    command = "update " + dest + " set "
    for col in range(0, len(col_list)):
        command += col_list[col]  + "="  + MakeCommand(value_list[col])
        if col != len(col_list) -1:
            command += ", "
    if condition != "":
        command += " where " + condition
    
    #print(command)
    OperateDataBase(command)

def QueryData(select_list, source_list, condition=""):
    #cur.execute("Select * from employee")
    command = "Select "
    for select in range(0, len(select_list)):
        command += select_list[select] 
        if select != len(select_list) -1:
            command +=  ", "
    command += " from " 
    for source in range(0, len(source_list)):
        command += source_list[source]
        if source != len(source_list)-1:
            command += ", "
    if condition != "":
        command += " where " + condition

    #print(command)
    contents = QueryOperate(command)
    return contents


def DeleteData(dest):
    #cur.execute("delete from employee where ID=1" )
    command = "delete from " + dest
    OperateDataBase(command)


if __name__ == '__main__':

    QueryData(['SID', "Fname || ' ' || Lname", 'MidScore*0.4 + FinalScore*0.6'], ['Enrollment', 'STUDENT'])