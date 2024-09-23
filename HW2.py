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
    cur.execute('select CID from COURSE where Fname =' + MakeString(courseName))
    cid = cur.fetchone()[0]
    command = "update Enrollment set MidScore = " + str(Midterm) + " where SID = " + MakeString(studentID) + ' and ' + 'CID = ' + MakeString(cid)
    cur.execute(command)
    command = "update Enrollment set FinalScore = " + str(Final) + " where SID = " + MakeString(studentID) + ' and ' + 'CID = ' + MakeString(cid)
    #print(command)
    cur.execute(command)

def GetClassStudentGrade(cur, courseName):
    cur.execute('select CID from COURSE where Fname =' + MakeString(courseName))
    cid = cur.fetchone()[0]
    #print(cid)
    command = "select SID, Fname, Lname, MidScore, FinalScore from Enrollment, STUDENT where CID = " + MakeString(cid) + "and SID = StudentID"
    #print(command)
    cur.execute(command)
    grades = cur.fetchall()
    print(grades)


if __name__ == '__main__':
    conn, cur = openDatabase('database')
    #InsertStudentData(cur, 'D05', 'KAYLEE', 'SIMPSON', 3, '女')
    GetClassStudentGrade(cur, '計概')


    closeDatabase(conn)
