import sys
import os
import re

# Shared functions
def onboarding_error(value):
    if value == 'No Excel':
        print('''🚫 ERROR 🚫
    No Excel Detected
    ''')
    elif value == 'Invalid Env':
        print('''
🚫 ERROR 🚫
The environment you selected is invalid; Run the program again!
''')
    elif value == 'Invalid Version':
        print('''
🚫 ERROR 🚫
The version you selected is invalid; Run the program again!
''')
    elif  value == 'Incorrect Version':
        print('''
🚫 ERROR 🚫
The version you selected is incorrect; Run the program again!
''')
    sys.exit()

def get_excel_path():
    path = './Excels/'
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)) and '.xlsx' in file:
            excel_path = path + file
            return excel_path

def get_excel_name():
    path = './Excels'
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)) and '.xlsx' in file:
            excel_name = file
            excel_name_without_extension = excel_name.split('.xlsx')[0]
            return excel_name_without_extension

def dynamic_values_array(subject_array, template_array):
    dynamic_values_array = []
    i = 0
    if subject_array == []:
        while i < len(template_array):
            array = []
            template_matches = re.findall(r'\${(.*?)}', template_array[i])
            for value in template_matches:
                array.append(value)
            array = set(array)
            array = list(array)
            dynamic_values_array.append(array)
            i += 1  
    else:
        while i < len(subject_array):
            array = []
            subject_matches = re.findall(r'\${(.*?)}', subject_array[i])
            for value in subject_matches:
                array.append(value)
            template_matches = re.findall(r'\${(.*?)}', template_array[i])
            for value in template_matches:
                array.append(value)
            array = set(array)
            array = list(array)
            dynamic_values_array.append(array)
            i += 1
    return dynamic_values_array

def file_generation(app_name, file_name, file_content, extension):
    if file_content == 0:
        print(f'{file_name}: File Not Required')
    else:
        with open(f'./Artifacts/{app_name}-{file_name}.txt', 'w') as file:
            file.write(file_content)
        
        txt_file = os.path.join('./Artifacts/', f'{app_name}-{file_name}.txt')
        output_file = txt_file.replace('.txt', extension)
        os.rename(txt_file, output_file)
        print(f'{file_name}: File Generation Completed')        
