from flask import Flask,render_template,request,session,redirect
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = 'shivadabhade'

conn = mysql.connector.connect(

    host = 'localhost',
    user = 'root',
    password = 'your_Mysql_password',
    database = 'your_database_name'
)



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginCheck',methods=['post'])
def loginCheck():
    cursor = conn.cursor(buffered=True)
    email = request.form['email']
    password = request.form['password']
    cursor.execute('select * from admin where email= %s',(email,))
    originalPassword = cursor.fetchone()
    cursor.close()
    if originalPassword and originalPassword[1]==email and originalPassword[2] == password :
        session['user'] = originalPassword[0] # this is username
        return redirect('/dashboard')
    else:
        return render_template('login.html',error='invalide username or password')
    # return render_template('dashboard.html')


@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html',user=session['user'])
    else:
        return render_template('login.html')

@app.route('/singUp')
def singUp():
    return render_template('singUp.html')

@app.route('/signUpCheck',methods=['post'])
def signUpCheck():
    username = request.form['userName']
    email = request.form['email']
    password = request.form['password']
    
    hasUpper = False
    hasSpecialCh = False

    specialChar = '!@#$%&'
    

    for ch in password:
        if ch in specialChar:
         hasSpecialCh=True
        if ch.isupper():
            hasUpper = True

    if not hasSpecialCh or not hasUpper:
        return render_template('singUp.html',error='Please enter 1 special charector and 1 upper case letter in password ')
    cursor = conn.cursor(buffered=True)
    try:    
        cursor.execute('insert into admin values (%s,%s,%s)',(username,email,password)) 
        conn.commit()
        cursor.close()
        session['user'] = username
        return redirect('/dashboard')  
    except Exception  as e:
        print(e)
        return render_template('singUp.html') 
    

@app.route('/viewStudent')
def viewStudent():
    cursor = conn.cursor(buffered=True)
    cursor.execute('select * from student')
    students = cursor.fetchall()
    cursor.close()

    return render_template('view_students.html', students=students)



@app.route('/addStudent')
def addStudent():
    return render_template('add_student.html')

@app.route('/addStudentDB',methods=['post'])
def addStudentDB():
    Roll_No = request.form['rollNo']
    Name = request.form['name']
    Branch = request.form['branch']
    Year = request.form['year']
    Mark = request.form['mark']
    try:
     cursor = conn.cursor(buffered=True)
     cursor.execute('insert into student values(%s,%s,%s,%s,%s)',(Roll_No,Name,Branch,Year,Mark))
     conn.commit()
     cursor.close()
     return redirect('/viewStudent') 
    except Exception as e:
      print('this is ',e)
    return render_template('dashboard.html')



@app.route('/viewremoveStudent')
def viewremoveStudent():
    cursor = conn.cursor(buffered=True)
    cursor.execute('select * from student')
    students = cursor.fetchall()
    cursor.close()
    return render_template('viewRemoveData.html',students=students)

@app.route('/removeStudent/<int:rollNo>')
def removeStudent(rollNo):
    Roll_No = rollNo
    cursor = conn.cursor(buffered=True)
    cursor.execute('delete from student where Roll_No=%s',(rollNo,))
    cursor.close()
    return redirect('/viewStudent')
    # return f'rollno is {rollNo}'


@app.route('/viewUpdateStudent')
def viewUpdateStudent():
    cursor = conn.cursor(buffered=True)
    cursor.execute('select * from student')
    students = cursor.fetchall()
    cursor.close()
    return render_template('viewUpdateStudent.html',students=students)

@app.route('/updatestudent/<int:rollNo>')
def updatestudent(rollNo):
    cursor = conn.cursor(buffered=True)
    cursor.execute('select * from student where Roll_No=%s',(rollNo,))
    student = cursor.fetchone()
    
    return render_template('updateStudent.html',student=student)

@app.route('/addUpdatedStudentDB',methods=['post'])
def addUpdatedStudentDB():
    Roll_No = request.form['rollNo']
    Name = request.form['name']
    Branch = request.form['branch']
    Year = request.form['year']
    Mark = request.form['mark']
    cursor = conn.cursor(buffered=True)
    cursor.execute('update student set Name=%s,Branch=%s,Year=%s,Mark=%s where Roll_No=%s',(Name,Branch,Year,Mark,Roll_No))
    conn.commit()
    cursor.close()
    return redirect('/viewStudent')
    
@app.route('/logOut')
def logOut():
    session.pop('user',None)
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True, port=3000)
