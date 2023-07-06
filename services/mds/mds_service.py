def pop_svc_converter(pop_svc_array):
    clean_pop_svc_array = []
    for item in pop_svc_array:
        item = item.split('[')[-1].split(']')[0]
        if item != 'Template ID':
            clean_pop_svc_array.append(item)
    return clean_pop_svc_array

def main_name_converter(table_name_array):
    converted_table_name_array = []
    for table_name in table_name_array:
        table_name = table_name.replace('_main', '')
        if table_name == 'audit_code' or table_name == 'audit_infotype':
            converted_table_name_array.append(table_name)
        elif table_name.split('_')[0] == 'cd':
            table_name = table_name.replace('_', '')
            converted_table_name_array.append(table_name + '_main')
        else:
            converted_table_name_array.append(table_name + '_main')
    return converted_table_name_array

def field_array_splitter(table_name_column_array, field_column_array):
    field_arrays = []
    field_array = []
    i = 0
    while i < len(field_column_array):
        if i == 0:
            field_array.append(field_column_array[i])
        elif table_name_column_array[i] == 'nan' and table_name_column_array[i - 1] == 'nan' or table_name_column_array[i] == 'nan' and table_name_column_array[i - 1] != 'nan':
            field_array.append(field_column_array[i])
        else:
            field_arrays.append(field_array)
            field_array = []
            field_array.append(field_column_array[i])
        i += 1
    field_arrays.append(field_array)
    return field_arrays