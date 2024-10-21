from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/test/login', methods=['GET', 'POST'])
def login():
    #  利用request取得使用者端傳來的方法為何
    if request.method == 'POST':
                          #  利用request取得表單欄位值
        return 'Hello ' + request.values['username']
    
    #  非POST的時候就會回傳一個空白的模板
    return render_template('login.html')
    

@app.route('/addclass')
def addclass():
   return render_template('addclass.html')

@app.route('/addenrollment')
def addenrollment():
   return render_template('addenrollment.html')

@app.route('/insertscore')
def insertscore():
   return render_template('insertscore.html')

@app.route('/searchscore')
def searchscore():
   return render_template('searchscore.html')

@app.route('/addstudent', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        stData={}
        stData['SID'] = request.values['sid']
        stData['sname'] = request.values['sname']
        stData['grade'] = request.values['grade']
        stData['student-sex'] = request.values['student-sex']
        print("stData = ", stData)
        
 
    return render_template('addstudent.html')

if __name__ == '__main__':
    app.debug = True
    app.run()  