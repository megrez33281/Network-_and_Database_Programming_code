import sqlite3

def openDatabase(name):
    conn=sqlite3.connect ('./' + name.replace('.db', '') +  '.db')
    cur=conn.cursor()
    return conn, cur

def closeDatabase(conn):
    conn.commit()
    conn.close()

def MakeString(a_str):
    return "'" + str(a_str) + "'"

def DatabaseCommand(cur, command):
    cur.execute ("create table USER2 (ID, NAME)")

def InsertStudentData(cur, studentID, FirstName, LastName, grade, gender):
    command = "Insert into STUDENT Values(" + MakeString(studentID) + ',' + MakeString(FirstName) + ',' + MakeString(LastName) + ','  +  str(grade) + ',' + MakeString(gender) +")"
    #print(command)
    cur.execute(command)

def InsertClassData(cur, courseID, courseName):
    command = "Insert into COURSE Values(" + MakeString(courseID) + ',' + MakeString(courseName) + ")"
    #print(command)
    cur.execute(command)

def InsertStudentClassData(cur, studentID, courseID):
    command = "Insert into Enrollment Values(" + MakeString(studentID) + ',' + MakeString(courseID) + ", 0, 0)"
    #print(command)
    cur.execute(command)

def InsertStudentGrade(cur, studentID, courseName, Midterm, Final):
    cur.execute('select CID from COURSE where Cname =' + MakeString(courseName))
    cid = cur.fetchone()[0]
    command = "update Enrollment set MidScore = " + str(Midterm) + ' ,' + " FinalScore = " + str(Final) +   " where SID = " + MakeString(studentID) + ' and ' + 'CID = ' + MakeString(cid)
    cur.execute(command)
    #command = "update Enrollment set FinalScore = " + str(Final) + " where SID = " + MakeString(studentID) + ' and ' + 'CID = ' + MakeString(cid)
    #print(command)
    #cur.execute(command)

def GetClassStudentGrade(cur, courseName):
    cur.execute('select CID from COURSE where Cname =' + MakeString(courseName))
    cid = cur.fetchone()[0]
    command = "select SID, Fname, Lname, Grade, Sex, MidScore*0.4 + FinalScore*0.6 from Enrollment, STUDENT where CID = " + MakeString(cid) + "and SID = StudentID"
    #print(command)
    cur.execute(command)
    grades = cur.fetchall()
    print("學號\t姓名\t年級\t性別\t總成績")
    for grade in grades:
        print(grade[0], grade[1] + ' ' + grade[2], grade[3], grade[4], grade[5])
    print()

def clear(cur):
    cur.execute('delete  from student')
    cur.execute('delete from  COURSE')
    cur.execute('delete from Enrollment')


if __name__ == '__main__':
    conn, cur = openDatabase('database')
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
            InsertStudentData(cur, command_list[1], command_list[2], command_list[3], command_list[4], command_list[5])
        
        elif command_type == 'b' and len(command_list) == 3:
            InsertClassData(cur, command_list[1], command_list[2])

        elif command_type == 'c' and len(command_list) == 3:
            InsertStudentClassData(cur, command_list[1], command_list[2])

        elif command_type == 'd' and len(command_list) == 5:
            InsertStudentGrade(cur, command_list[1], command_list[2], command_list[3], command_list[4])
        
        elif command_type == 'e' and len(command_list) == 2:
            GetClassStudentGrade(cur, command_list[1])

        elif command_type == '-1':
            break
        
        else:
            print("錯誤的指令！")

        command = input("請輸入指令：")
        
    closeDatabase(conn)
