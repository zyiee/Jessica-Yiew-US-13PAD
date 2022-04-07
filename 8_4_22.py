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
def update():
    line1 = student_data['name']
    line1_format = line1[1:]
    line2 = student_data['possible mark']  
    line2_format = line2[2:]
    test_format = line1[2:]
    return line1, line1_format, line2, line2_format, test_format

line1, line1_format, line2, line2_format, test_format = update()

#print(student_data)
#print(line1_format)
#print(line2_format)
#print(test_format)

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

def test_lower():
    test_lowered = []
    y = 0
    for items in test_format:
        test_lowered.append(test_format[y].lower())
        y = y + 1
    return test_lowered
#test_initial = test_lower()
#test_input = test_initial.extend(test_format) #all inputs
test_lowered = test_lower() #lowered test list

def save_file(): #converts the dictionary and lists within code into suitable format to save into txt file
    with open(open_file[1], 'w') as file:
        for value in student_data:
            format_list = []
            data = student_data[value]
            format_list.extend(data)
            format_list.insert(1, value)
            startstr = " "
            for items in format_list:
                startstr = startstr + str(items) + ','
            startstr = startstr.strip(',')
            startstr = startstr + '\n'
            file.write(startstr)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#info_input('Student name:\t')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~WRITE NEW STUDENT INTO FILE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def new_student(): #gathering data to write into file
    new_stud_id = []
    print('Format: Name, ID', *line1_format, sep = ', ') 
    new_name = info_input('Student name:\t')
    new_id = number_check('Student ID:\t')
    new_stud_id.append(str(new_id))
    new_gender = gender_check()
    new_stud_id.append(new_gender)
    y = 0
    for tests in test_format: #allows for test score entering based on how many tests exist within the system - also has set parameters
        while True:
            number_input = number_check(str(test_format[y] + ' parameters: ' + str(line2_format[y]) + '\t'))
            if number_input < 0 or number_input > int(line2_format[y]):
                print('Please enter a value within parameters')
                pass
            else:
                break
        new_stud_id.append(str(number_input))
        y = y + 1
    student_data[new_name] = new_stud_id #appends new info into dictionary
    base_format = '{},{},{},{},{}'
    new_studwrite = base_format.format(new_id, new_name, new_gender, new_stud_id[2], new_stud_id[3]) #base information
    if len(test_format) > 2: #if there are more than 2 tests in the system
        y = 1
        z = 4
        for brackets in test_format[2:]:
            modified = str(new_studwrite + ',{}')
            modified_studwrite = modified.format(new_stud_id[z])
            new_studwrite = modified_studwrite
            y = y + 1
            z = z + 1

#new_student()
#print(student_data)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~STUDENT LOOKUP~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def lookup(): #asks for user input to lookup student info in the system
    while True:
        name_input = info_input('Who are you looking for\t')
        name_lowered = name_input.lower()
        if name_lowered not in student_data: #validation
            print('Student not in system')
            pass 
        else: #formatting for printing
            base_format = 'Name: {}\nID: {}\nGender: {}\nTest A: {}\nTest B: {}\n'
            lookup_user = student_data[name_lowered]
            display = base_format.format(name_lowered, lookup_user[0], lookup_user[1], lookup_user[2], lookup_user[3]) #base information - 5 values
            if len(test_format) == 2: #if there are only 2 tests in the system
                print(display)
            if len(test_format) > 2: #if there are more than 2 tests in the system
                x = 2
                z = 4
                for brackets in test_format[2:]:
                    add_bracket = str(test_format[x] + ': ' + '{}\n') #adds a new line to format
                    modified = str(display + add_bracket) #display + new line
                    print(lookup_user)
                    modified_display = modified.format(lookup_user[z]) #formats info
                    display = modified_display #ensures that display is always updated as the loop goes
                    x = x + 1
                    z = z + 1         
                print(display)
            return name_lowered

#lookup()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~INFO CHANGE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#test info starts from 2 on a list
def info_change(): #asks user using
    student = lookup()
    student_info = student_data[student]
    while True:
        option = info_input('Which test would you like to change\t')
        option_lowered = option.lower()
        if option_lowered not in test_lowered:
            print('Please choose from the options below')
            print(*test_format, sep = ', ')
            pass
        else:
            index = test_lowered.index(option_lowered)
            break
    d_index = 2 + index
    while True:
        print(str(option + ' parameters:\t' + line2_format[index]))
        change_mark = number_check('Enter value\t')
        if change_mark < 0 or change_mark > int(line2_format[index]):
            print(str('Please enter within the parameters of 0 - ' + line2_format[index]))
            pass
        else:
            student_info[d_index] = str(change_mark)
            print(str(option + ' for' + student + ' has been changed to ' + str(change_mark)))
            break
    
#info_change()    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ADD TEST~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add_test():
    test_add = info_input('What test would you like to add?\t')
    while True:
        parameter_add = number_check('What is the max possible mark?\t')
        if parameter_add < 0:
            print('Please enter a positive value')
            pass
        else:
            student_data['name'].append(test_add)
            student_data['possible mark'].append(parameter_add)
            break

#add_test()            
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DISPLAY STATISTICS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def test_statistics():
    while True:
        stat_input = info_input('What test statistics would u like to view?\t')
        stat_lowered = stat_input.lower()
        if stat_lowered not in test_lowered:
            print('Please choose from the options below')
            print(*test_format, sep = ', ')
            pass
        else:
            names_list = []
            scores_list = []
            index = test_lowered.index(stat_lowered)
            f_index = 2 + index
            print(student_data)
            for students, value in student_data.items():
                names_list.append(students)
                test_value = value[f_index]
                scores_list.append(test_value)
                print(str(students + ': ' + test_value))
            
            #highest score
            highest = scores_list[2]
            for items in scores_list[1:]:
                if items > highest:
                    highest = items
            
            #lowest score
            lowest = scores_list[2]
            for items in scores_list[1:]:
                if items < lowest:
                    lowest = items
            
            #average score
            clean_list = []
            total_score = sum([int(i) for i in scores_list[2:] if type(i)== int or i.isdigit()])
            scores_clean = [i for i in scores_list[2:] if type(i) == int or i.isdigit()]
            print(total_score)
            average = total_score/len(scores_clean)
            print(str(stat_input + ' average class score: ' + str(round(average))))
            break
            
test_statistics()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CODE RUNNING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def run():
    while True:
        action_input = info_input('What do you intend to do?\nOptions --> 1: Add New student\t2: Change student info\t3: Add new test\t4: Statistics\n')
        if action_input in op1:
            new_student()
            break
        elif action_input in op2:
            info_change()
            break
        elif action_input in op3:
            add_test()
            break
        elif action_input in op4:
            test_statistics()
            break
        else:
            print('Invalid input')
            pass
    line1, line1_format, line2, line2_format, test_format = update()
    return line1, line1_format, line2, line2_format, test_format

#line1, line1_format, line2, line2_format, test_format = run()
#print(test_format)
#while True:    
    #more = info_input('Would you like to do anything else?\t')
    #if more in y_list:
        #line1, line1_format, line2, line2_format, test_format = run()
        #print(test_format)
    #elif more in n_list:
        #print('ty')
        #save_file()
        #print(student_data)
        #print(test_format)
        #break
    #else:
        #print('Invalid input')
        #pass


    

    

    
    

