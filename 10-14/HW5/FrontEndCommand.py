from DataBaseCommand import InsertData, UpdateData, QueryData, DeleteData, MakeIndex, getIndex

def initialize():
    if getIndex("student") == 0:
        print("Make student's index")
        MakeIndex("Student", ["Fname", "Lname", "Grade", "Sex", "Email", "photo"],["SID"])

    if getIndex("course") == 0:
        print("make course's index")
        MakeIndex("course", ["CID", "Cname"])
    
    if getIndex('Enrollment') == 0:
        print("make Enrollment's index")
        MakeIndex("Enrollment", ["MidScore", "FinalScore"], ["SID", "CID"])
    
    
def InsertStudentData(studentID, Fname, Lname, grade, gender, email, photo):
    #A. 新增學生資料
    photo_id = InsertData('image', {"Data":photo})
    InsertData('STUDENT', {"SID":studentID, "Fname": Fname, "Lname": Lname, "Grade": grade, "Sex": gender, "Email":email, "photo": photo_id})

def InsertClassData(courseID, courseName):
    #B. 新增課程資料
    InsertData('COURSE',{ "CID":courseID, "Cname":courseName})

def InsertStudentClassData(studentID, courseID):
    #C. 新增選課資料
    InsertData('Enrollment', {"SID":studentID, "CID":courseID, "MidScore":0, "FinalScore":0})

def UpdateGrade(studentID, Cname, MidScore, FinalScore):
    #D. 新增成績
    courseID = QueryCID(Cname)
    UpdateData("Enrollment", {"SID":studentID, "CID":courseID}, {"MidScore":MidScore, "FinalScore":FinalScore})


def QueryCID(courseName):
    datas = QueryData("Course", {"Cname":courseName})
    return datas[0]['CID']


def GetClassStudentGrade(courseName):
    #E. 查詢總成績
    CourseID = QueryCID(courseName)
    CourseDatas = QueryData("Enrollment", {"CID":CourseID})
    student_list = []
    for student in CourseDatas:
        #取得期中期末成績
        student_list.append({"SID":student['SID'], "MidScore":student['MidScore'], "FinalScore": student['FinalScore'], "TotalScore":int(student['MidScore'])*0.4 + int(student['FinalScore'])*0.6})
    print("Student List = ", student_list)
    student_list_detail = []
    for student in student_list:
        #取得學生資料
        student_data = QueryData("STUDENT", {"SID": student['SID']})[0]
        student_list_detail.append({"photo":student_data['photo'], "SID":student['SID'], "Name":student_data['Fname'] + " " + student_data["Lname"], "MidScore":student["MidScore"], "FinalScore":student["FinalScore"], "TotalScore":student["TotalScore"], "Email":student_data["Email"]})
    
    return student_list_detail


def getSIDFromEnrollment():
    datas = QueryData("Enrollment", {})
    a_set = set()
    for data in datas:
        a_set.add(data["SID"])
    a_list = []
    for data in a_set:
        a_list.append(data)
    return a_list

def getCnameFromEnrollment(StudentID):
    #找到學生修的所有課程
    datas = QueryData("Enrollment", {"SID":StudentID})
    CourseNames = []
    for data in datas:
        CourseName = QueryData("Course", {"CID":data["CID"]})[0]
        #print(CourseName)
        CourseNames.append(CourseName["Cname"])
    return CourseNames

def getCIDFromEnrollment(StudentID):
    datas = QueryData("Enrollment", {"SID":StudentID})
    student_lists = []
    for data in datas:
        student_lists.append([data['CID']])
    return student_lists

def getAllCourse():
    datas = QueryData("Course", {})
    course_list = []
    for data in datas:
        course_list.append([data["CID"], data["Cname"]])
    return course_list

def getAllStudentID():
    datas = QueryData("Student", {})
    student_list = []
    for data in datas:
        student_list.append([data["SID"]])
    return student_list

def getPicture(pic_id):
    datas = QueryData("image", {"_id":pic_id})
    return datas[0]['Data']
    
def clear():
    DeleteData('student')
    DeleteData('COURSE')
    DeleteData('Enrollment')
    DeleteData('image')



if __name__ == '__main__':
    {}
    #clear()
    #InsertStudentData('D02', 'THOMAS', 'TUCKER', 3, '男', 'XXXXXXXXXX', '123456')
    #InsertClassData('C01', '計概')
    #InsertStudentClassData('D01', 'C01')
    #UpdateGrade("D01", "計概", 100, 50)
    #print(GetClassStudentGrade("計概"))
    #MakeIndex("Student", ["Fname", "Lname", "Grade", "Sex", "Email", "photo"],["SID"])
    #initialize()
    #print(getCnameFromEnrollment("D01"))
    print(getAllStudentID())
    