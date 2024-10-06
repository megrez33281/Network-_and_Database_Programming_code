from DataBaseCommand import InsertData, UpdateData, QueryData, DeleteData

def AddComma(content):
    return "'" + str(content) + "'"

def InsertStudentData(studentID, Fname, Lname, grade, gender, email):
    #A. 新增學生資料
    InsertData('STUDENT', [studentID, Fname, Lname, int(grade), gender, email])

def InsertClassData(courseID, courseName):
    #B. 新增課程資料
    InsertData('COURSE', [courseID, courseName])

def InsertStudentClassData(studentID, courseID):
    #C. 新增選課資料
    InsertData('Enrollment', [studentID, courseID])


def QueryCID(courseName):
    return QueryData(["CID"], ["COURSE"], "Fname = " + courseName)[0]

def UpdateMidterm(studentID, courseName, score):
    #D. 輸入期中成績
    cid = QueryCID(courseName)
    UpdateData('Enrollment', ['MidScore'], [int(score)], "SID = " + AddComma(studentID) + ' and ' + 'CID = ' + AddComma(cid))

def UpdateFinal(studentID, courseName, score):
    #F. 輸入期末成績
    cid = QueryCID(courseName)
    UpdateData('Enrollment', ['FinalScore'], [int(score)], "SID = " + AddComma(studentID) + ' and ' + 'CID = ' + AddComma(cid))


def GetClassStudentGrade(courseName):
    #G. 查詢總成績
    cid = QueryCID(courseName)
    grades = QueryData(["SID", "Fname || ' ' || Lname, MidScore*0.4 + FinalScore*0.6"], ["Enrollment", "STUDENT"], "CID = " + AddComma(cid) + "and SID = StudentID")[0]
    return grades

def getAllStudentID():
    studentsID = QueryData(["StudentID"], ["STUDENT"])
    return studentsID

def getAllCourse():
    Courses = QueryData(["CID", "Cname"], ["COURSE"])
    return Courses

    
def clear():
    DeleteData('student')
    DeleteData('COURSE')
    DeleteData('Enrollment')


if __name__ == '__main__':
    {}

    #InsertStudentData('D01', 'THOMAS', 'TUCKER', 3, '男', 'XXXXXXXXXX')
    #InsertClassData('C01', '計概')
    #InsertStudentClassData('D01', 'C01')

    