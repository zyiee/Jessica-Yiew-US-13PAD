import os
def open_files():
    file_directory = os.listdir('.')
    file_options = []
    
    for i in range(len(file_directory)):
        if '.csv' in file_directory[i]:
            file_options.append(file_directory[i])
        elif '.txt' in file_directory[i]:
            file_options.append(file_directory[i])
    while True:
        file_input = input(str(file_options) + '\nPlease choose a file to open\t')
        try:
            open_file = open(file_input)
            break
        except IOError as e:
            print('Cannot open file')
            pass
    return open_file
        

open_file = open_files()
student_data = {}

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


        