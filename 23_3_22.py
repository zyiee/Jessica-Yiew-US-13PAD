import os
def open_files():
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
        except IOError as e:
            print('Cannot open file')
            pass
    return open_file
        

open_file = open_files()
student_data = {}
yn_list = ['yes','Yes','Y','y','N', 'no','n', 'No']
y_list = ['yes','y','Yes','Y']
n_list = ['no','n','No','N']

def file_split():
    with open_file as f:
        next(f)
        next(f)
        for lines in f: #for lines in file it formats everything into dictionary and list
            values = lines.split(',') #splits info 
            key = values[1].lower()
            values.pop(1)
            student_data[key] = values
            
file_split()     
print(student_data)

def student_search():
    while True:
        name_input = str(input('Who are you looking for?\t'))
        if name_input in student_data:
            return name_input
        else:
            new_entry = str(input('Does not exist within system. Add to system?\t'))
            while new_entry not in yn_list:
                print('Invalid')
                new_entry = str(input('Does not exist within system. Add to system?\t'))
            if new_entry in n_list:
                print('Thanks for nothing')
                pass
            elif new_entry in y_list:
                break

student_search()