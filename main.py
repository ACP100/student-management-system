import json
import os
import sys

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(current_dir,"src"))

from src import *

class person:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

class teacher(person):
    def __init__(self, teacher_id, subject):
        super().__init__(None , None ,None ,None ,)
        self.teacher_id = teacher_id
        self.subject = subject
    
    def update_marks():
        """This function is used to uupdate the marks of students who are aalready registered.

        Args:
            student_name (string): _description_. Defaults to input("enter name of student").
        """
       
        student_name = input("enter name of student")
        with open("data/student.json", 'r+') as f:
                student_data = json.load(f) #student_data has all the contents of the file 
                for i in student_data:
                    if i['name'] == student_name:
                        print("enter updated marks")
                        i['subject']['maths'] = input("enter updated marks for maths")
                        i['subject']['science'] = input("enter updated marks for science")
                        i['subject']['social'] = input("enter updated marks for social")
                        i['subject']['english'] = input("enter updated marks for english")
                        #student_data has been updated
                
                f.seek(0) #takes the pointer to front of the file
                json.dump(student_data, f, indent=4)#dumps the updated cotents to the file
                f.truncate()#limits the file size to that of student_data
               
    def add_new_student():
        """This function is used by teacher to add new students
        """
        print("Add details of students")
        name = input("Enter Name")
        Rollno = generate.generate_rollno(name)
        Address = input("Enter Address")
        phone = input("Enter Phone Number")
        b=check.phone_check(phone)#to check vaidity of phone number
        while b == False:
            print("Re-enter the phone number")
            phone = input("Enter Phone Number")
            b=check.phone_check(phone)
        email = input("Enter Email")
        a=check.email_check(email)#to check validity of email
        while a == False:#to ensure that email is accepted only when the email of correct format is providedd 
            print("Re-enter email")
            email = input("Enter email")
            a=check.email_check(email)
        print("enter marks")
        m =int( input("enter marks of maths"))
        s = int(input("enter marks of science"))
        so= int( input("enter marks of social"))
        e = int(input("enter marks of english\n"))

        with open("data/student.json", 'r+') as f:
            student_data = json.load(f)
            new_student = {
                    "name": name,
                    "Rollno": Rollno,
                    "Address": Address,
                    "phone": phone,
                    "email": email,
                    "subject": {"maths": m, "science": s, "social" : so , "english" : e},
                    "percentage" : ((m+s+so+e)/400)*100
                }
            student_data.append(new_student)
            f.seek(0)
            json.dump(student_data, f, indent=4)
            f.truncate()

    def students_overview():
        """this function displays overview of details of all studets.It includes 
        student's name, address, roll number and email 
        """
        with open ("data/student.json" , 'r') as f:
            detail = json.load(f)
            
            for i in detail:
                print(f"Name : {i['name']}")
                print(f"Address : {i['Address']}")
                print(f"Roll Number : {i['Rollno']}")
                print(f"Phone Number : {i['phone']}")
                print(f"Email : {i['email']}")
                print("\n \n \n")
    
    def students_individual():
        """this function shows every dettail of a specific studet
        """
        student_name = input("Enter Name of the student you wat to seee details of:")
        with open ("data/student.json" , 'r') as f:
            detail = json.load(f)
            
            for  i in  detail:
                print(i['name'])
                found = True
                if i['name'] == student_name:
                    print(f"Name : {i['name']}")
                    print(f"Address : {i['Address']}")
                    print(f"Roll Number : {i['Rollno']}")
                    print(f"Phone Number : {i['phone']}")
                    print(f"Email : {i['email']}")
                    print(f"Marks : {i['subject']}")
                    print(f"Percentage : {i['percentage']}")
                    print("\n \n \n")
                    founnd = True
                
                if not found:
                    print("Enter a valid name")  
                    teacher.students_individual()
    
    def delete_student():
        """this function deletes a student from the database"""
        student_name = input("enter nme of studet you want to delete")
        with open ("data/student.json" , 'r') as f:
            data = json.load(f)
            list1 = []
            for i in data:
                if i['name'] == student_name:
                    print(i)
                else:
                    list1.append(i) 
                    
        print("studet deleted")
        with open ("data/student.json" , 'w') as f:
            json.dump(list1 , f , indent =4)
        
    
        name_list = [i['name'].lower() for i in list1] # put all the 'names' in the file in name_list list
        name_list = sorted(name_list)
        
        for i, name in enumerate(name_list):
           
            for student in list1:
                if student['name'].lower() == name:
                    student['Rollno'] = i + 1
                    
        
        
        with open ("data/student.json" , 'r+') as f:

             json.dump(list1 , f , indent = 4)
        


                    
    def sign_up():
        """this functionn adds new teachers
        """
        a = True
        b = True
        c = True
        name = input("Enter your name")
        subject = input("Entre your subject")
        phone = input("Enter phone number")
        b=check.phone_check(phone)
        while b == False:
            print("Re-enter the phone number")
            phone = input("Enter Phone Number")
            b=check.phone_check(phone)
        email = input("Enter Email")
        a=check.email_check(email)#to check validity of email
        while a == False:#to ensure that email is accepted only when the email of correct format is providedd 
            print("Re-enter email")
            email = input("Enter email")
            a=check.email_check(email)
        address = input("Enter your address")
        password = input("Enter password for login ")
        confirm_password = input("re-enter password for login ")
        if password != confirm_password:
            print("password doesn't match")
            c = False
        while c == False:
            confirm_password = input("re-Enter password ")
            if password != confirm_password:
                print("password doesn't match")
                c = False
            else:
                c = True 
        teacher_id = generate.generate_id(subject)
        print(f"Your teacher id is: {teacher_id}")
        
        with open("data/teacher.json", 'r+') as f:
                teacher_data = json.load(f)
                new_teacher = []
                new_teacher = {
                    "name": name,
                    "subject": subject,
                    "phone number": phone,
                    "address": address,
                    "email": email,
                    "password":password,
                    "subject": subject,
                    "id" : teacher_id
                }
                teacher_data.append(new_teacher)
                f.seek(0)
                json.dump(teacher_data, f, indent=4)
                f.truncate()    
   
    def teacher_log_in(self):
        """this function is used by teacher to log in ad access teacher functions
        """
        with open ('data/teacher.json' , 'r+') as f:
            data = json.load(f)
            TeacherID = input("Enter your TeacherID")
            
            for i in data:
                if i["id"] == TeacherID:
                    pw = input("enter password")
                    x = 'y'
                    while x != 'n':
                        if i['password'] == pw:
                            print(f"welcome , {i['name']}")

                            self.name = i['name']
                            self.teacher_id = i['id']
                            teacher_login = teacher(self.teacher_id, None)
                            teacher_login.teacher_functions()
                        else:
                            x = input("Invalid password, do you want to re-enter password? y/n")
                              
    def teacher_functions(self):
        """all the ffunctions techers can perform are accessed from here
        """
    
        x = input ("press 1 to add new student\npress 2 to see students overview\npress 3 to view student  detail \npress 4 to update marks\npress 5 to deete student data\n")

        if x == "1":
            teacher.add_new_student()
        elif x == "2":
            teacher.students_overview()
        elif x == "3":
            teacher.students_individual()
        elif x == "4":
            teacher.update_marks()
        elif x == "5":
            teacher.delete_student()
        elif x ==0:
            exit
        else:
            x = 0
            print("Invalid input. Please try again.")
            self.teacher_functions()

class student(person):
    def __init__ (self, rollno, marks):
        super().__init__(None , None ,None ,None ,)
        self.rollno = rollno

    def pass_fail_determination(self):
        """this function determines weather the sttudent is pass or fail
        """
        with open ("data/student.json" , 'r') as f:
            data = json.load(f)

        for i in data:
            if i['Rollno'] == self.rollno:
                if i['subject']['maths'] < 40 or i['subject']['science'] < 40 or i['subject']['english'] < 40 or i['subject']['social'] < 40:
                    print(f"{i['name']}, you have failed") 
                else:
                    print(f"{i['name']}, you have passed")

    def rank(self):
        """this functtion ranks the studets based on their percenttage
        """
        with open("data/student.json", 'r') as f:
            data = json.load(f)
        
            sorted_students = sorted(data, key=lambda x: x['percentage'], reverse=True) # Sorts the list of students in descending order based on their percentage scores

            for i, student in enumerate(sorted_students):
                print(f"Rank {i+1}: {student['name']} - {student['percentage']}%")

    def marks(self):
        """this function is used toview all the marks of the student
        """
        with open ("data/student.json" , 'r') as f:
            data = json.load(f)
            for i in data:
                if i['Rollno'] == self.rollno:
                    print(f"science = {i['subject']['science']}\nmaths = {i['subject']['maths']}\nenglish = {i['subject']['english']}\nsocial = {i['subject']['social']}")        
             
    def percentage(self):
        """this function is used to view the percentage of the student"""
        with open ("data/student.json" , 'r') as f:
            data = json.load(f)

        for i in data:
            if i['Rollno'] == self.rollno:
                print(f"You have recieved {i['percentage']}%")

    def student_functions(self):
        """this function is used to view all the functions of the student"""
       
        x = int(input("\n\n\npress 1 to view your percentge\npress 2 to view rank of all students\npress 3 to view highest and the lowest marks\npress 4 to determine your pass/fail status\npress 5 to view your marks\npress 0 to continue\n"))
        if x == 1:
            self.percentage()
        elif x == 2:
            self.rank()
        elif x == 3:
            highest_lowest_marks_finder.Highest_lowest_marks(self.name)
        elif x == 4:
            self.pass_fail_determination()
        elif x == 5:
            self.marks()
        elif x ==0:
            exit
        else:
            print("Invalid input. Please try again.")   
            self.student_functions()

    def student_log_in(self):
        """this function is used to log in the student"""
        RollNo_for_login =int(input("Enter your Roll Number"))
        with open ('data/student.json' , 'r') as f:
            data = json.load(f)
            found = False
            for i in data:
                    if i['Rollno'] == RollNo_for_login:    
                        found = True                           
                        print("Welcome to your dashboard")
                        self.name = i['name']
                        self.rollno = i['Rollno']
                        student_login = student(self.rollno, None)
                        self.student_functions()
            
            if not found:
                print("Roll number not found. Please try again.")
                self.student_log_in()

def log_in():
    """this function is used to log in the user"""
    x = input("Are you a Student or Teacher?")
    x=(x.strip()).lower()
    try:
        if x == "student":
            studentobj = student(None , None)
            studentobj.student_log_in()
            
        if x ==  "teacher":
            teacherobj = teacher(None, None  )
            teacherobj.teacher_log_in()
            
        else: 
            raise Exception ("Invalid input. Try again")
    except Exception as e: 
        print(f"Error: {e}")

log = input("log in or sign up?")
log=(log.strip()).lower()
try:
    if log == 'log in':
        log_in()
    elif log == 'sign up':
        teacher.sign_up()
    else :
        raise Exception ("Invalid input. Try again")

except Exception as e: 
    print(f"Error: {e}")





