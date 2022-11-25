from flask import Flask, render_template, redirect, url_for, request
import cx_Oracle
import Employee as emp
import Student as stud
app = Flask(__name__)
@app.route('/', methods=['GET'])
def login1():
    return render_template('login.html')
    
@app.route('/login', methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')
@app.route('/ehome', methods=['GET'])
def ehome():
    try:
        con = cx_Oracle.connect('scott/tiger@localhost')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM emp order by empno")
        result = cursor.fetchall()
        print('count of records:',len(result))
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e) 
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()
    headers = ['Empno','Ename','Sal']            
    return render_template('ehome.html',headers=headers,objects=result)
@app.route('/shome', methods=['GET'])
def shome():
    try:
        con = cx_Oracle.connect('scott/tiger@localhost')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM student")
        result = cursor.fetchall()
        print('count of records:',len(result))
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e) 
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()
    headers = ['RollNo','StudentName','Fee']            
    return render_template('shome.html',headers=headers,objects=result)

@app.route('/chome', methods=['GET'])
def chome():
    try:
        con = cx_Oracle.connect('scott/tiger@localhost')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM COURSE order by cname")
        result = cursor.fetchall()
        print('count of records:',len(result))
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e) 
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()
    headers = ['CID','CourseName','Duration','Fee']            
    return render_template('chome.html',headers=headers,objects=result)
@app.route('/cinsert', methods=['GET'])
def cinsert():
    return render_template('cinsert.html');
@app.route('/addcourse', methods=['POST'])
def addcourse():
    if request.method == 'POST':
        cname = request.form['cname']
        duration = request.form['Duration']
        fee = request.form['Fee']
        print(cname,duration,fee)
        try:
            con = cx_Oracle.connect('scott/tiger@localhost')
            cursor = con.cursor()
            cursor.execute("INSERT INTO course values(cseq.nextval,:cname,:duration,:fee)",(cname,duration,fee))
            con.commit();
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e) 
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()
        return redirect(url_for('chome'))

@app.route('/deletecourse/<cid>',methods=['GET'])
def deletecourse(cid):
    try:
        con = cx_Oracle.connect('scott/tiger@localhost')
        cursor = con.cursor()
        cursor.execute("delete from course where cid ="+str(cid))
        con.commit();
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e) 
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()
    return redirect(url_for('chome'))

@app.route('/upcourse',methods=['POST'])
def upcourse():
    if request.method == 'POST':
        cname = request.form['cname']
        duration = request.form['Duration']
        fee = request.form['Fee']
        cid = request.form['cid']
        print(cname,duration,fee)
        try:
            con = cx_Oracle.connect('scott/tiger@localhost')
            cursor = con.cursor()
            cursor.execute("UPDATE course SET cname=:cname,duration=:duration,fee=:fee where cid=:cid",(cname,duration,fee,cid))
            con.commit();
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e) 
        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()
        return redirect(url_for('chome'))

@app.route('/updatecourse/<cid>',methods=['GET'])
def updatecourse(cid):
    try:
        con = cx_Oracle.connect('scott/tiger@localhost')
        cursor = con.cursor()
        cursor.execute("select * from course where cid ="+str(cid))
        result = cursor.fetchall()
        return render_template('updatecourse.html',objects=result)
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e) 
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()
    return redirect(url_for('chome'))    
@app.route('/einsert', methods=['GET'])
def einsert():
    return render_template('einsert.html');

@app.route('/empinsert',methods=['POST'])
def empinsert():
    if request.method == 'POST':
        ename = request.form['ename']
        sal = request.form['sal']
        e = emp.Employee()
        e.insert_employee(ename,sal)
        return redirect(url_for('ehome'))
    
@app.route('/sinsert', methods=['GET'])
def sinsert():
    return render_template('sinsert.html');

@app.route('/studinsert',methods=['POST'])
def studinsert():
    if request.method == 'POST':
        name = request.form['name']
        efees = request.form['efees']
        s = stud.Student()
        s.insert_student(name,efees)
        return redirect(url_for('shome'))

if __name__ == '__main__':  
   app.run(debug = True)  

