import cx_Oracle

class Student:
    def __init__(self):
            
        self.con = None;
        self.cursor = None;
        
    def open(self):
        try:
            self.con = cx_Oracle.connect('scott/tiger@localhost')
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
            
    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.con:
                self.con.close()
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)
            
    
    def insert_student(self,name,efees):
        try:
            self.open()
            self.cursor = self.con.cursor()
            self.cursor.execute("INSERT INTO student values(sseq.nextval,:name,:efees)",(name,efees))
            self.con.commit();
            return True
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e) 
        finally:
            self.close()
        return False

    def update_student(self,srollno,name,efees):
        try:
            self.open()
            self.cursor = self.con.cursor()
            self.cursor.execute("update student set name =:name, efees=:efees where srollno=:srollno",(name,efees,srollno))
            self.con.commit();
            return True
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e) 
        finally:
            self.close()
        return False
    
    def delete_student(self,empno):
        try:
            self.open()
            self.cursor = self.con.cursor()
            self.cursor.execute("delete from student where srollno ="+str(srollno))
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
            self.cursor.execute("SELECT * FROM student")
            result = self.cursor.fetchall()
            return result
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e) 
        finally:
            self.close()
        return None
    def select_student_by_id(self,srollno):
        try:
            self.open()
            self.cursor = self.con.cursor()
            self.cursor.execute("SELECT * FROM student where srollno ="+str(srollno))
            result = self.cursor.fetchall()
            return result
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e) 
        finally:
            self.close()
        return None
        
            


            
            
