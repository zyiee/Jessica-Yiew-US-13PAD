import os
student_data = {}

# yes no lists
yn_list = ['yes', 'Yes', 'Y', 'y', 'N', 'no', 'n', 'No']
y_list = ['yes', 'y', 'Yes', 'Y']
n_list = ['no', 'n', 'No', 'N']

# option lists
op1 = ['1', 'new student', 'New student', 'Add new student', 'add new student']
op2 = ['2', 'student info', 'Student info', 'Change student info', 'change student info']
op3 = ['3', 'add new test', 'Add new test', 'new test', 'New test']
op4 = ['4', 'statistics', 'Statistics', 'stats', 'Stats']


def open_files():  # opens required files to run a program from program directory
    file_directory = os.listdir('.')  # looks in folder file
    file_options = []  # gives no. of eligible files to open to run program with
    for i in range(len(file_directory)):
        if '.csv' in file_directory[i]:  # if csv files are in directory
            file_options.append(file_directory[i])
        elif '.txt' in file_directory[i]:  # if txt files are in directory
            file_options.append(file_directory[i])
    while True:
        file_input = input(str(file_options) + '\nPlease choose a file to open\t')  # user input for file opening
        try:  # validation
            open_file = open(file_input)
            break
        except IOError:
            print('Cannot open file')
            pass
    return open_file, file_input  # returns file path and open input


def file_split():  # opens file and splits every line to put into dictionary
    with open_file[0] as f:
        lines = [line.strip() for line in f]
        y = 0
        for items in lines:
            info = lines[y].split(',')
            key = info[1].lower()
            info.pop(1)
            student_data[key] = info
            y = y + 1


def update():  # updates variables to call
    line1 = student_data['name']  # student data values, otherwise the 1st line of csv file ***updated[0]***
    line1_format = line1[1:]  # format for new student entry - can be used if multiple tests exist within the system ***updated[1]***
    line2 = student_data['possible mark']  # 2nd line of csv file ***updated[2]***
    line2_format = line2[2:]  # possible marks for each test ***updated[3]***
    test_format = line1[2:]  # tests that exists within system ***updated[4]***
    return line1, line1_format, line2, line2_format, test_format


def info_input(user_input):  # general user input collection
    info = str(input(user_input))
    return info  # returns user input


def gender_check():  # gender check to reject anything thats not f or m
    while True:
        gender_input = info_input('Student Gender:\t')
        gender_input = gender_input.lower()
        if gender_input not in ['f', 'm']:
            print('Please enter either f or m')
            pass
        else:
            break
    return gender_input  # returns user gender input


def number_check(user_input):  # general number checker
    while True:
        try:
            number_info = int(input(user_input))
            break
        except ValueError:
            print('Not a number value')
    return number_info  # returns user number input


def test_lower():  # ease of input for test list
    test_lowered = []
    y = 0
    for items in updated[4]:
        test_lowered.append(updated[4][y].lower())
        y = y + 1
    return test_lowered  # returns list of lowered tests


def save_file():  # converts the dictionary and lists within code into suitable format to save into txt file
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


def lookup():  # student lookup
    while True:  # searching for only first or last name
        try:
            name_input = info_input('Who are you looking for\t')
            name_input = name_input.lower()
            name_data = [items for name, items in student_data.items() if name.startswith(name_input) or name.endswith(name_input)][0]
            break
        except IndexError:
            print('Student not in system')
    for key, value in student_data.items():  # finding full name to display
        if name_data == value:
            name = key
            break
    base = 'Name: {}\nID: {}\nGender: {}\n'  # print displaying
    display = base.format(name, name_data[0], name_data[1], name_data[2], name_data[3])
    y = 0
    z = 2
    for tests in updated[4]:
        display_format = str(display + updated[4][y] + ': {}\n')
        display = display_format.format(name_data[z])
        z = z + 1
        y = y + 1
    print(display)
    return name  # returns student full name


def new_student():  # gathering data to write into file
    new_stud = []
    print('Format: Name, ID', *updated[1], sep=', ')
    new_firstname = info_input('Student first name:\t')
    new_lastname = info_input('Student last name:\t')
    new_name = new_firstname + ' ' + new_lastname
    new_id = number_check('Student ID:\t')
    new_stud.append(str(new_id))
    new_gender = gender_check()
    new_stud.append(new_gender)
    y = 0
    for tests in updated[4]:  # allows for test score entering based on how many tests exist within the system - also has set parameters
        while True:
            score_input = number_check(str(updated[4][y] + ' parameters: ' + str(updated[3][y]) + '\t'))
            if score_input < 0 or score_input > int(updated[3][y]):
                print('Please enter a value within parameters')
                pass
            else:
                break
        new_stud.append(str(score_input))
        y = y + 1
    student_data[new_name] = new_stud  # appends new info into dictionary


def add_test():  # adds new test into dictionary
    print('Existing tests: ')
    print(*updated[4], sep=', ')
    new_test = info_input('What test would you like to add?\t')
    while True:  # parameter check
        new_parameter = number_check('What is the max possible mark?\t')
        if new_parameter < 0:
            print('Please enter a positive value')
            pass
        else:
            student_data['name'].append(new_test)
            student_data['possible mark'].append(str(new_parameter))
            for students in student_data:  # appends absent by default
                if students != 'name' and students != 'possible mark':
                    student_data[students].append('a')
            break


def info_change():  # student info change
    name = lookup()
    student_info = student_data[name]
    while True:  # asks what test to change
        print(*updated[4], sep=', ')
        option = info_input('Which test would you like to change\t')
        option = option.lower()
        if option not in test_lowered:
            print('Please choose from the options below')
            pass
        else:
            index = test_lowered.index(option)
            break
    d_index = 2 + index  # index of test change on student info list
    while True:  # parameter check
        print(str(option + ' parameters:\t' + updated[3][index]))
        change_mark = number_check('Enter value\t')
        if change_mark < 0 or change_mark > int(updated[3][index]):
            print(str('Please enter within the parameters of 0 - ' + updated[3][index]))
            pass
        else:
            student_info[d_index] = str(change_mark)
            print(str(option + ' for ' + name + ' has been changed to ' + str(change_mark)))
            break


def test_statistics():  # test statistics display
    while True:  # asks what test to view
        print(*updated[4], sep=', ')
        stat_input = info_input('What test statistics would u like to view?\t')
        stat_input = stat_input.lower()
        if stat_input not in test_lowered:
            print('Please choose from the options below')
            pass
        else:
            break
    names_list = []
    scores_list = []
    index = test_lowered.index(stat_input)
    f_index = 2 + index
    for students, value in student_data.items():  # gets score list for all students
        names_list.append(students)
        test_value = value[f_index]
        scores_list.append(test_value)
        print(str(students + ': ' + test_value))

    # highest score
    highest = scores_list[2]
    for items in scores_list[2:]:
        if items > highest:
            if type(items) == int or items.isdigit():
                highest = items
    try:
        int(highest)
    except ValueError:
        highest = 0

    # lowest score
    lowest = scores_list[2]
    for items in scores_list[2:]:
        if items < lowest:
            lowest = items
    try:
        int(lowest)
    except ValueError:
        lowest = 0

    # average score
    total_score = sum([int(i) for i in scores_list[2:] if type(i) == int or i.isdigit()])
    scores_clean = [i for i in scores_list[2:] if type(i) == int or i.isdigit()]
    try:
        average = total_score / len(scores_clean)
    except ZeroDivisionError:  # if there is no collective score
        average = 0

    # gender average
    f_scores = []  # female collective scores
    m_scores = []  # male collective scores
    for students in student_data:
        value = student_data[students]
        gender = value[1].lower()
        if gender == 'f':
            f_scores.append(value[f_index])
        elif gender == 'm':
            m_scores.append(value[f_index])

    # female average
    total_f = sum([int(i) for i in f_scores if type(i) == int or i.isdigit()])  # sums all scores excluding absent
    clean_f = len([i for i in f_scores if type(i) == int or i.isdigit()])  # gets the number of students who have scores that arent absent
    try:
        f_average = total_f / clean_f
    except ZeroDivisionError:  # if there is no collective score
        f_average = 0

    # male average
    total_m = sum([int(i) for i in m_scores if type(i) == int or i.isdigit()])  # sums all scores excluding absent
    clean_m = len([i for i in m_scores if type(i) == int or i.isdigit()])  # gets number of students who have scores that arent absent
    try:
        m_average = total_m / clean_m
    except ZeroDivisionError:  # if there is no collective score
        m_average = 0

    print(str('Average class score: ' + str(round(average))))  # average
    print(str('Highest score: ' + str(highest)))  # highest score
    print(str('Lowest score: ' + str(lowest)))  # lowest score
    print(str('Female average: ' + str(round(f_average))))  # female average
    print(str('Male average: ' + str(round(m_average))))  # male average


def action():  # what does the user want to do?
    while True:
        option = info_input('What do you intend to do?\nOptions --> 1: Add New student\t2: Change student info\t3: Add new test\t4: Statistics\n')
        if option in op1:  # new student
            new_student()
            break
        elif option in op2:  # change info
            info_change()
            break
        elif option in op3:  # add test
            add_test()
            break
        elif option in op4:  # view test statistics
            test_statistics()
            break
        else:
            print('Invalid input')
            pass
    updated = update()  # updates variables
    test_lowered = test_lower()  # updates tests


open_file = open_files()
file_split()
updated = update()
test_lowered = test_lower()
action()
save_file()
