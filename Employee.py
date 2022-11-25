import cx_Oracle

class Employee:
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
            
    
    def insert_employee(self,ename,sal):
        try:
            self.open()
            self.cursor = self.con.cursor()
            self.cursor.execute("INSERT INTO emp values(eseq.nextval,:ename,:sal)",(ename,sal))
            self.con.commit();
            return True
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e) 
        finally:
            self.close()
        return False

    def update_employee(self,empno,ename,sal):
        try:
            self.open()
            self.cursor = self.con.cursor()
            self.cursor.execute("update emp set ename =:ename, sal=:sal where empno=:empo",(empno,ename,sal))
            self.con.commit();
            return True
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e) 
        finally:
            self.close()
        return False
    
    def delete_employee(self,empno):
        try:
            self.open()
            self.cursor = self.con.cursor()
            self.cursor.execute("delete from emp where empno ="+str(empno))
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
            self.cursor.execute("SELECT * FROM emp")
            result = self.cursor.fetchall()
            return result
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e) 
        finally:
            self.close()
        return None
    def select_emp_by_id(self,emp):
        try:
            self.open()
            self.cursor = self.con.cursor()
            self.cursor.execute("SELECT * FROM emp where empno ="+str(empno))
            result = self.cursor.fetchall()
            return result
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e) 
        finally:
            self.close()
        return None
    def getTable(result,header):
        table="<tr>"
        for col in header:
            table += "<th>" +str(col) +"</th>"
        table +="</tr>"            
            
        for row in result:
            table +="<tr>"
            trow ="<tr>"
            for c in row:
                trow += "<td>" + str(c) +"</td>"
            trow +="</tr>"
        table += trow
        return table

    
            
            
            


            
            
