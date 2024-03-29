import re

def nan_remover(array):
    if array == []:
        return array
    elif isinstance(array[0], list):
        no_nan_array = []
        for item in array:
            no_nan_item = list(filter(lambda x: x != 'nan', item))
            no_nan_array.append(no_nan_item)
    else:
        no_nan_array = list(filter(lambda x: x != 'nan', array))
    return no_nan_array

def query_template_cleaner(array, service):
    clean_template_array = []
    for item in array:
        item = re.sub(r'\$\((\w+)\)', r'${\1}', item)
        if service == 'MDS' or service == 'MPDS':
            item = item.replace('"${', '${').replace('}"', '}').split("\n")
            item = ' '.join(line.lstrip() for line in item)
            item = re.sub(r'(\$\{.*?\}|".*?")|([a-zA-Z_]+)', lambda match: match.group(1) if match.group(1) else match.group(2).lower(), item)
        clean_template_array.append(item)
    return clean_template_array

def subject_cleaner(array, service):
    clean_subject_array = []
    for item in array:
        item = re.sub(r'\$\((\w+)\)', r'${\1}', item)
        if service == 'MCNS':
            item = item.split("\n")
            item = ' '.join(line.lstrip() for line in item)
            item = item.replace('\t', '    ')
            item = item.replace('\\', '\\\\')
            item = item.replace(r'"', r'\"')
        clean_subject_array.append(item)
    return clean_subject_array

def template_cleaner(array, service, channel_type_array):
    clean_template_array = []
    i = 0
    if service == 'MCNS':
        while i < len(array):
            if channel_type_array[i] == 'email' or channel_type_array[i] == 'push':
                item = array[i]
                item = re.sub(r'\$\((\w+)\)', r'${\1}', item)
                item = item.replace('\t', '    ').replace('\\', '\\\\')
                item = item.split("\n")
                item = ' '.join(line.lstrip() for line in item)
                item = item.replace(r'"', r'\"')
                clean_template_array.append(item)
            else:
                line_array = []
                item = array[i]
                item = re.sub(r'\$\((\w+)\)', r'${\1}', item)
                item = item.replace('\n', '')
                item = item.replace(r'\n', '\n')
                item = item.split('\n')
                for line in item:
                    line.replace('\t', '    ').replace('\\', '\\\\')
                    line_array.append(line)
                item = '\\n'.join(line.lstrip() for line in line_array)
                item = item.replace(r'"', r'\"')
                clean_template_array.append(item)                
            i += 1
    return clean_template_array

def dynamic_values_array_generator(subject_array, template_array):
    dynamic_values_array = []
    if subject_array == [] and template_array == []:
        dynamic_values_array.append([])
    
    i = 0
    if subject_array == []:
        while i < len(template_array):
            array = []
            template_matches = re.findall(r'\${(.*?)}', template_array[i])
            for value in template_matches:
                array.append(value)
            array = set(array)
            array = list(array)
            array.sort()
            dynamic_values_array.append(array)
            i += 1  
    elif template_array == []:
        while i < len(subject_array):
            array = []
            template_matches = re.findall(r'\${(.*?)}', subject_array[i])
            for value in template_matches:
                array.append(value)
            array = set(array)
            array = list(array)
            array.sort()
            dynamic_values_array.append(array)
            i += 1  
    else:
        while i < len(template_array):
            array = []
            subject_matches = re.findall(r'\${(.*?)}', subject_array[i])
            for value in subject_matches:
                array.append(value)
            template_matches = re.findall(r'\${(.*?)}', template_array[i])
            for value in template_matches:
                array.append(value)
            array = set(array)
            array = list(array)
            array.sort()
            dynamic_values_array.append(array)
            i += 1
    return dynamic_values_array
