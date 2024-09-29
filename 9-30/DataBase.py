import sqlite3

database_name = 'database'
def openDatabase(name):
    conn=sqlite3.connect ('./' + name.replace('.db', '') +  '.db')
    cur=conn.cursor()
    return conn, cur

def closeDatabase(conn):
    conn.commit()
    conn.close()

def MakeString(a_str):
    return "'" + str(a_str) + "'"

def DatabaseCommand(command):
    conn, cur = openDatabase(database_name)
    cur.execute ("create table USER2 (ID, NAME)")
    closeDatabase(conn)

def InsertStudentData(studentID, Fname, Lname, grade, gender):
    conn, cur = openDatabase(database_name)
    command = "Insert into STUDENT Values(" + MakeString(studentID) + ',' + MakeString(Fname) + ',' + MakeString(Lname) + ','  +  str(grade) + ',' + MakeString(gender) +")"
    #print(command)
    cur.execute(command)
    closeDatabase(conn)

def InsertClassData(courseID, courseName):
    conn, cur = openDatabase(database_name)
    command = "Insert into COURSE Values(" + MakeString(courseID) + ',' + MakeString(courseName) + ")"
    #print(command)
    cur.execute(command)
    closeDatabase(conn)

def InsertStudentClassData(studentID, courseID, MidScore, FinalScore):
    conn, cur = openDatabase(database_name)
    command = "Insert into Enrollment Values(" + MakeString(studentID) + ',' + MakeString(courseID) + ',' + MakeString(MidScore) + ',' + MakeString(FinalScore) + ")"
    #print(command)
    cur.execute(command)
    closeDatabase(conn)

def InsertStudentGrade(studentID, courseName, Midterm, Final):
    conn, cur = openDatabase(database_name)
    cur.execute('select CID from COURSE where Cname =' + MakeString(courseName))
    cid = cur.fetchone()[0]
    command = "update Enrollment set MidScore = " + str(Midterm) + ' ,' + " FinalScore = " + str(Final) +   " where SID = " + MakeString(studentID) + ' and ' + 'CID = ' + MakeString(cid)
    cur.execute(command)
    #command = "update Enrollment set FinalScore = " + str(Final) + " where SID = " + MakeString(studentID) + ' and ' + 'CID = ' + MakeString(cid)
    #print(command)
    #cur.execute(command)
    closeDatabase(conn)

def GetClassStudentGrade(courseName):
    conn, cur = openDatabase(database_name)
    cur.execute('select CID from COURSE where Cname =' + MakeString(courseName))
    cid = cur.fetchone()[0]
    command = "select SID, Fname || ' ' || Lname, MidScore*0.4 + FinalScore*0.6 from Enrollment, STUDENT where CID = " + MakeString(cid) + "and SID = StudentID"
    #print(command)
    cur.execute(command)
    grades = cur.fetchall()
    closeDatabase(conn)
    return grades

def getAllStudentID():
    conn, cur = openDatabase(database_name)
    command = "select StudentID from STUDENT"
    #print(command)
    cur.execute(command)
    studentsID = cur.fetchall()
    closeDatabase(conn)
    return studentsID

def getAllCourse():
    conn, cur = openDatabase(database_name)
    command = "select CID, Cname from COURSE"
    #print(command)
    cur.execute(command)
    Courses = cur.fetchall()
    closeDatabase(conn)
    return Courses

    
def clear():
    conn, cur = openDatabase(database_name)  
    cur.execute('delete  from student')
    cur.execute('delete from  COURSE')
    cur.execute('delete from Enrollment')
    closeDatabase(conn)


if __name__ == '__main__':
    #clear(cur)
    print("指令說明\n")
    print("a 新增學生資料：a 學號\t姓名\t年級\t性別")
    print("b 新增課程資料：b 課程號碼\t課名")
    print("c 新增選課資料：c 學號\t課程代碼")
    print("d 輸入期中期末成績： d 學號\t課名\t期中成績\t期末成績")
    print("e 查詢總成績： e 課名")
    print("結束程式：-1\n\n")
    command = input("請輸入指令：")
    while command != -1:
        command_list = command.split(" ")
        command_type = command_list[0]
        if command_type == 'a' and len(command_list) == 6:
            InsertStudentData(command_list[1], command_list[2], command_list[3], command_list[4], command_list[5])
        
        elif command_type == 'b' and len(command_list) == 3:
            InsertClassData(command_list[1], command_list[2])

        elif command_type == 'c' and len(command_list) == 3:
            InsertStudentClassData(command_list[1], command_list[2])

        elif command_type == 'd' and len(command_list) == 5:
            InsertStudentGrade(command_list[1], command_list[2], command_list[3], command_list[4])
        
        elif command_type == 'e' and len(command_list) == 2:
            GetClassStudentGrade(command_list[1])

        elif command_type == '-1':
            break
        
        else:
            print("錯誤的指令！")

        command = input("請輸入指令：")
        

