from flask import Flask, request, render_template, redirect
import FrontEndCommand

app = Flask(__name__)
courseName = ""

@app.route('/test/login', methods=['GET', 'POST'])
def login():
    #  利用request取得使用者端傳來的方法為何
    if request.method == 'POST':
                          #  利用request取得表單欄位值
        return 'Hello ' + request.values['username']
    
    #  非POST的時候就會回傳一個空白的模板
    return render_template('login.html')
    

@app.route('/addclass', methods=['GET', 'POST'])
def addclass():
   if request.method == 'POST':
        cData={}
        cData['cid'] = request.values['cid']
        cData['cname'] = request.values['cname']
        FrontEndCommand.InsertClassData(cData['cid'], cData['cname'])
        return render_template('addclass.html', cData=cData)
   return render_template('addclass.html')

@app.route('/addenrollment', methods=['GET', 'POST'])
def addenrollment():
    Sid_list = FrontEndCommand.getAllStudentID()
    courses = FrontEndCommand.getAllCourse()
    course_dict = {}
    for course in courses:
       course_dict[course[0]] = course[1]
    if request.method == 'POST':
        cData={}
        cData['sid'] = request.values['sid']
        cData['cid'] = request.values['cid']
        FrontEndCommand.InsertStudentClassData(cData['sid'], cData['cid'])
        return render_template('addenrollment.html', sDatas=Sid_list, course_dict=course_dict, course_list=courses, cData=cData)
    return render_template('addenrollment.html', sDatas=Sid_list, course_dict=course_dict, course_list=courses)

@app.route('/insertscore', methods=['GET', 'POST'])
def insertscore():
   Student_list = FrontEndCommand.getAllStudentID()
   Course_List = FrontEndCommand.getAllCourse()
   if request.method == 'POST':
        scoreData={}
        scoreData['sid'] = request.values['sid']
        scoreData['cname'] = request.values['cname']
        scoreData['midterm'] = request.values['midterm']
        scoreData['final'] = request.values['final']
        FrontEndCommand.UpdateMidterm(scoreData['sid'], scoreData['cname'], scoreData['midterm'])
        FrontEndCommand.UpdateFinal(scoreData['sid'], scoreData['cname'], scoreData['final'])
        return render_template('insertscore.html', Student_list = Student_list, Course_List = Course_List, scoreData=scoreData)

   return render_template('insertscore.html', Student_list = Student_list, Course_List = Course_List)

@app.route('/searchscore', methods=['GET', 'POST'])
def searchscore():
   Course_List = FrontEndCommand.getAllCourse()
   if request.method == 'POST':
        global courseName
        courseName = request.values['cname']
        return redirect('scorelist')

   return render_template('searchscore.html', Course_List=Course_List)

@app.route('/scorelist', methods=['GET', 'POST'])
def scorelist():
    print("Search Name", courseName)
    grades= FrontEndCommand.GetClassStudentGrade(courseName)
    grade_data = []
    for grade in grades:
        grade_data.append(grade[0] + "||" + grade[1] + "||" + grade[2] + "||" + str(grade[3]))
    page_data_number = 5
    show_page_number = 6
    return render_template('scorelist.html', courseName=courseName, page_data_number=page_data_number, grades=grade_data, show_page_number=show_page_number)

@app.route('/addstudent', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        stData={}
        stData['SID'] = request.values['sid']
        stData['sname'] = request.values['sname']
        stData['grade'] = request.values['grade']
        stData['student-sex'] = request.values['student-sex']
        Fname, Lname = stData['sname'].split(" ")
        FrontEndCommand.InsertStudentData(stData['SID'], Fname, Lname, stData['grade'], stData['student-sex'])
        print("stData = ", stData)
        return render_template('addstudent.html', stData=stData)
        
 
    return render_template('addstudent.html')

if __name__ == '__main__':
    app.debug = True
    app.run()  