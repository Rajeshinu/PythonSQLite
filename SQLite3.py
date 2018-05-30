import sqlite3
conn=sqlite3.connect(':memory:')  #memory: will allows you create a temporary sqlitedb file in RAM and will be deleted automatically once the program is completed we can use any file name to be created here

c=conn.cursor()

c.execute("""CREATE TABLE Employee (name text,job text,sal integer)""")

def addemp(name,job,sal):
    with conn:
        c.execute("INSERT INTO Employee VALUES(?,?,?)",(name,job,sal),)

def getempbyall():
    with conn:
         c.execute("SELECT * FROM Employee ")
         l1=c.fetchall()
         for i in l1:
            print(i)

def getempbyname(name):
    with conn:
         c.execute("SELECT * FROM Employee WHERE name=:name",{'name':(name)})
         l1=c.fetchall()
         for i in l1:
            print(i)


def updateemp(name,job,sal):
    with conn:
        c.execute("UPDATE Employee SET sal=:sal, job=:job WHERE first=:first",{'sal':(sal),'job':(job),'first':(name)})

def delemp(name):
    with conn:
        c.execute("DELETE from  Employee WHERE first=:first",{'first':(name)})



filename=str(input("Please enter the File name to be created"))


count=1
while count==1:
 opt=int(input("""please select the
                option 1 to add new emp details:
                option 2 to edit emp details:
                option 3 to view emp details:
                option 4 to all view emp details
                option 5 to delete emp details:
                option 0 to exit:"""))
 if opt==1:
    print("Please enter the employee details ")
    empname=str(input("Employee Name: "))
    empjob=str(input("Employee Designation: "))
    empsal=int(input(" Employee Salary: "))
    addemp(empname,empjob,empsal)
    print("Employee details updated succesfully ")

 elif opt==2:
    print("please enter the emp name and details ")
    empname=str(input("Employee Name: "))
    empjob=str(input("Employee Designation: "))
    empsal=int(input(" Employee Salary: "))
    updateemp(empname,empjob,empsal)

 elif opt==3:
    getname=str(input("please enter the emp name and detials "))
    getempbyname(getname)

 elif opt==4:
    getempbyall()

 elif opt==5:
    delempname=str(input("please enter the emp name to be deleted "))
    delemp(delempname)
 elif opt==0:
    count=0
    pass

conn.close()


