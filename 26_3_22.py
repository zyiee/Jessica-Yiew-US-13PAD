import os
student_data = {}

#----yes no validation----
yn_list = ['yes','Yes','Y','y','N', 'no','n', 'No']
y_list = ['yes','y','Yes','Y']
n_list = ['no','n','No','N']

#----options ease of use----
op1 = ['1', 'new student', 'New student', 'Add new student', 'add new student']
op2 = ['2', 'student info', 'Student info', 'Change student info', 'change student info']
op3 = ['3', 'add new test', 'Add new test', 'new test', 'New test']
op4 = ['4', 'statistics', 'Statistics', 'stats', 'Stats']

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~FILE OPENING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
    return open_file, file_input
        
def file_split(): #opens file and splits every line to put into dictionary
    with open_file[0] as f:
        lines = [line.strip() for line in f]
        y = 0
        for items in lines:
            info = lines[y].split(',')
            key = info[1].lower()
            info.pop(1)
            student_data[key] = info
            y = y + 1

open_file = open_files() #creates a list for the 2 returned functions - 1 is to open the file and the other is a str form            
file_split()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~VALIDATION AND EASE OF USE DEFINITIONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#----printing format purposes----
line1 = student_data['name']
line1_format = line1[1:]
line2 = student_data['possible mark']  
line2_format = line2[2:]
test_format = line1[2:]

print(student_data)
print(line1_format)
print(line2_format)
print(test_format)

def info_input(user_input): #general user input collection
    info = str(input(user_input))
    return info

def gender_check(): #gender check to reject anything thats not f or m
    while True:
        gender_input = info_input('Student Gender:\t')
        if gender_input not in ['f', 'F', 'M', 'm']:
            print('Please enter either f or m')
            pass
        else:
            break
    return gender_input
    
def number_check(user_input): #general number checker
    while True:
        try:
            number_info = int(input(user_input))
            break
        except ValueError:
            print('Not a number value')
    return number_info
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~WRITE NEW STUDENT INTO FILE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def new_student(): #gathering data to write into file
    new_stud_id = []
    print('Format: Name', *line1_format, sep = ',')
    new_name = info_input('Student name:\t')
    new_id = number_check('Student ID:\t')
    new_stud_id.append(str(new_id))
    new_gender = gender_check()
    new_stud_id.append(new_gender)
    y = 0
    for tests in test_format: #allows for test score entering based on how many tests exist within the system - also has set parameters
        while True:
            test_input = number_check(str(test_format[y] + ' parameters: ' + line2_format[y] + '\t'))
            if test_input < 0 or test_input > int(line2_format[y]):
                print('Please enter a value within parameters')
                pass
            else:
                break
        new_stud_id.append(str(test_input))
        y = y + 1
    student_data[new_name] = new_stud_id #appends new info into dictionary
    base_format = '{},{},{},{},{}'
    new_studwrite = base_format.format(new_id, new_name, new_gender, new_stud_id[2], new_stud_id[3]) #base information
    if len(test_format) == 2: #if there are only 2 tests in the system
        with open(open_file[1], 'a') as file_write:
            file_write.write('\n' + str(new_studwrite))
            file_write.close
    if len(test_format) > 2: #if there are more than 2 tests in the system
        y = 1
        z = 4
        for brackets in test_format[2:]:
            add_bracket = str(',{}'*y)
            modified = str(new_studwrite + add_bracket)
            modified_studwrite = modified.format(new_stud_id[z])
            y = y + 1
            z = z + 1
        with open(open_file[1], 'a') as file_write:
            file_write.write('\n' + str(modified_studwrite))
            file_write.close

#new_student()
#print(student_data)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~STUDENT LOOKUP~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def lookup():
    while True:
        name_input = info_input('Who are you looking for\t')
        if name_input not in student_data:
            print('Student not in system')
            pass #placeholder
        else:
            base_format = 'ID: {}\nName: {}\nGender: {}\nTest A: {}\nTest B: {}'
            display = base_format.format(student_data[0], user_input, student_data[1], student_data[2], student_data[3]) #base information - 5 values
            if len(test_format) == 2: #if there are only 2 tests in the system
                print(display)
            if len(test_format) > 2: #if there are more than 2 tests in the system
                y = 1
                z = 4
                for brackets in test_format[2:]:
                    add_bracket = str(',{}'*y)
                    modified = str(new_studwrite + add_bracket)
                    modified_studwrite = modified.format(new_stud_id[z])
                    y = y + 1
                    z = z + 1         
            print(student_data[name_input])
            break
        
        
lookup()
    
#def user_action():
    #while True:
        #action_input = info_input('What do you intend to do?\nOptions --> 1: Add New student\t2: Change student info\t3: Add new test\t4: Statistics')
        #if action_input in op1:
            #new_student()
        #elif action_input in op2:
            

    

    
    


            