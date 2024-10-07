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
    InsertData('Enrollment', [studentID, courseID, 0, 0])


def QueryCID(courseName):
    return QueryData(["CID"], ["COURSE"], "Cname = " + AddComma(courseName))[0][0]

def UpdateMidterm(studentID, courseName, score):
    #D. 輸入期中成績
    cid = QueryCID(courseName)
    #print(cid)
    UpdateData('Enrollment', ['MidScore'], [int(score)], "SID = " + AddComma(studentID) + ' and ' + 'CID = ' + AddComma(cid))

def UpdateFinal(studentID, courseName, score):
    #F. 輸入期末成績
    cid = QueryCID(courseName)
    UpdateData('Enrollment', ['FinalScore'], [int(score)], "SID = " + AddComma(studentID) + ' and ' + 'CID = ' + AddComma(cid))


def GetClassStudentGrade(courseName):
    #G. 查詢總成績
    cid = QueryCID(courseName)
    grades = QueryData(["SID", "Fname", "Lname", "MidScore*0.4 + FinalScore*0.6"], ["Enrollment", "STUDENT"], "CID = " + AddComma(cid) + " and SID = StudentID")
    return grades

def getAllStudentID():
    studentsID = QueryData(["StudentID"], ["STUDENT"])
    return studentsID

def getAllCourse():
    Courses = QueryData(["CID", "Cname"], ["COURSE"])
    return Courses

def getSIDFromEnrollment():
    datas = QueryData(["SID"], ["Enrollment"])
    a_set = set()
    for data in datas:
        a_set.add(data)
    a_list = []
    for data in a_set:
        a_list.append(data)
    return a_list

def getCnameFromEnrollment(SID):
    datas = QueryData(["CID"], ["Enrollment"], "SID = " + AddComma(SID))
    CourseNames = []
    for data in datas:
        CourseName = QueryData(["Cname"], ["Course"], "CID = " + AddComma(data[0]))[0][0]
        #print(CourseName)
        CourseNames.append(CourseName)
    return CourseNames

def getCIDFromEnrollment(SID):
    datas = QueryData(["CID"], ["Enrollment"], "SID = " + AddComma(SID))
    return datas

def getWarningList():
    #取得Reminder中所有資料
    WarningStudent = QueryData(["SID", "CID"], ["Reminder"])
    WarningList = []
    for warning in WarningStudent:
        student_data = QueryData(["Fname", "Lname", "MidScore", "Email"], ["student", "Enrollment"], "SID = " + AddComma(warning[0]) + " and CID = " + AddComma(warning[1]))[0]
        CourseName = QueryData(["Cname"], ["Course"], "CID = " + AddComma(warning[1]))[0][0]
        data_list = [student_data[0] + " " + student_data[1],  CourseName, student_data[2], student_data[3]]
        #print(data_list)
        WarningList.append(data_list)
    return WarningList
        
    
def clear():
    DeleteData('student')
    DeleteData('COURSE')
    DeleteData('Enrollment')
    DeleteData('Reminder')


if __name__ == '__main__':
    {}
    #clear()
    #InsertStudentData('D01', 'THOMAS', 'TUCKER', 3, '男', 'XXXXXXXXXX')
    #InsertClassData('C01', '計概')
    #InsertStudentClassData('D01', 'C01')
    #UpdateMidterm('D01', '計概', 100)
    #UpdateFinal('D01', '計概', 50)
    print(GetClassStudentGrade("計概")[0][2])


    