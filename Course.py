import cx_Oracle

class Course:
    def __init__(self):
            
        self.con = None;
        self.cursor = None;
        
    def open(self):
        try:
            if(self.con is None):
                self.con = cx_Oracle.connect('scott/tiger@localhost')
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
            
    def close(self):
        try:
            if self.cursor is not None:
                self.cursor.close()
            if self.con is not None:
                self.con.close()
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
            
    
    def insert_course(self,name,duration,fee):
        try:
            self.open()
            self.cursor = self.con.cursor()
            self.cursor.execute("INSERT INTO course values(cseq.nextval,:cname,:Duration,:fee)",(name,Duraiton,fee))
            self.con.commit();
            return True
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e) 
        finally:
            self.close()
        return False

    def update_course(self,cid,cname,duration,fee):
        try:
            self.open()
            self.cursor = self.con.cursor()
            self.cursor.execute("update course set cname =:cname,Duration= :duration ,fee=:fee where cid=:cid",(cname,duration,fee,cid))
            self.con.commit();
            return True
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e) 
        finally:
            self.close()
        return False
    
    def delete_course(self,cid):
        try:
            self.open()
            self.cursor = self.con.cursor()
            self.cursor.execute("delete from course where cid ="+str(cid))
            self.con.commit();
            return True
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e) 
        finally:
            self.close()
        return False
    
    def select_all(self):
        try:
            self.open()
            self.cursor = self.con.cursor()
            self.cursor.execute("SELECT * FROM course")
            result = self.cursor.fetchall()
            return result
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e) 
        finally:
            self.close()
        return None
    def select_course_by_id(self,cid):
        try:
            self.open()
            self.cursor = self.con.cursor()
            self.cursor.execute("SELECT * FROM course where cid ="+str(cid))
            result = self.cursor.fetchall()
            return result
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e) 
        finally:
            self.close()
        return None
    def select_student_by_course_id(self,cid):
        try:
            self.open()
            self.cursor = self.con.cursor()
            self.cursor.execute("SELECT srollno FROM student_course_details where cid ="+str(cid))
            result = self.cursor.fetchall()
            rolls=[]
            for row in result:
                rolls.append(row[0])
            studs =self.select_students_by_stud_id(rolls)
            return studs
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e) 
        finally:
            self.close()
        return None
    def select_students_by_stud_id(self,result):
        try:
            self.open()
            self.cursor = self.con.cursor()
            s=""
            for v in result:
                s += str(v) +","
            s +="0"                
                
            self.cursor.execute("SELECT * FROM student where srollno in("+ s +")")
            result = self.cursor.fetchall()
            return result
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle ", e) 
        return None
    def get_students_list(self,result):
        table ="<table><tr><th>RollNo</th><th>Name</th><th>Fee</th></tr>"
        for row in result:
            table +="<tr>"
            tcol =""
            for col in row:
                tcol +="<td>"+str(col)+"</td>"
            table += tcol +"</tr>"                
                
        table += "</table>"
        return table
        
        
        
        
c = Course()
c.select_student_by_course_id(15)



            
            
