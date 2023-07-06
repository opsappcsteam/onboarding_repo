def file_type_cleaner(row_array):
    clean_file_type_array = set()
    for file_type in row_array:
        if file_type == 'image/jpg (.jpg)':
            clean_file_type_array.add('image/jpeg')
        elif file_type != 'nan' and file_type != '(Select)':
            clean_file_type_array.add(file_type.split(' ')[0])
    clean_file_type_array  = list(clean_file_type_array)
    clean_file_type_array.sort()
    return clean_file_type_array