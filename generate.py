import json
def generate_id (subject):

    with open ('data/teacher.json' , 'r+') as f:
        data = json.load(f)
        n = 1
        for i in data:
            if i['subject'] == subject:
                n= n+1
        #to generate unique id for teacher consisting of first 3 letters of their subject and a unique number 
        subject= subject.upper()
        subject = subject[:3]    
        teacher_id = subject + str(n)
        return teacher_id
        



def generate_rollno(roll_name):
    with open("data/student.json", 'r+') as f:
        data = json.load(f)
        name_list = [i['name'].lower() for i in data] # put all the 'names' in the file in name_list list
        name_list.append(roll_name.lower())
        name_list = sorted(name_list)#sort the names 
        #updating the file
        for i, name in enumerate(name_list):
            for student in data:
                if student['name'].lower() == name:
                    student['Rollno'] = i + 1
        #to add roll number of  roll_nname to the file 
        for i,j in enumerate(name_list):
            if roll_name == j:
                return(i+1)

        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()


if __name__ =="__main__" :
    generate_rollno("aasy")
