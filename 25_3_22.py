import os
student_data = {}
#----yes no validation----
yn_list = ['yes','Yes','Y','y','N', 'no','n', 'No']
y_list = ['yes','y','Yes','Y']
n_list = ['no','n','No','N']

#----options ease of use----
op1 = ['1', 'new student', 'New student', 'Add new student', 'add new student']
op2 = ['2', 'student info', 'Student info', 'Change student info', 'change student info']
op3 = ['3', 'statistics', 'Statistics']

def open_files(): #opens required files to run a program from program directory
    file_directory = os.listdir('.') #looks in folder file
    file_options = [] #gives no. of eligible files to open to run program with
    
    for i in range(len(file_directory)):
        if '.csv' in file_directory[i]: #if csv files are in directory
            file_options.append(file_directory[i])
        elif '.txt' in file_directory[i]: #if txt files are in directory
            file_options.append(file_directory[i])
    while True:
        file_input = input(str(file_options) + '\nPlease choose a file to open\t') #user input for file opening
        try: #validation
            open_file = open(file_input) 
            break
        except IOError:
            print('Cannot open file')
            pass
    return open_file

        
def file_split(): #opens file and splits every line to put into dictionary
    with open_file as f:
        for lines in f: #for lines in file it formats everything into dictionary and list
            values = lines.split(',') #splits info 
            key = values[1].lower()
            values.pop(1)
            student_data[key] = values       

open_file = open_files()            
file_split()

#----printing format purposes----
line1 = student_data['name']
line1_format = line1[1:]
line2 = student_data['possible mark']  
print(student_data)


def new_student(): #gathering data to write into file
    new_studformat = '{},{},{},{}'
    print('Format: Name', *line1_format, sep = ',')
    new_name = str(input('Student name:\t'))
    new_id = str(input('Student ID:\t'))
    new_gender = str(input('Student Gender:\t'))
    
    

#def user_action():
    #while True:
        #action_input = str(input('What do you intend to do?\nOptions --> 1: Add New student\t2: Change student info\t3: Statistics'))
        #if action_input in op1:
            