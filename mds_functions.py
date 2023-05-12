import re

def mds_array(df, value):
    array = []
    for index, row in df.iterrows():
        i = 0
        while i < len(df.columns):
            if row[i] == value and value == 'Template ID':
                if row[i + 3] == '<This will be filled up by AppCS Onboarding Team>' or str(row[i + 3]) == 'nan':
                    output_str = '<placeholder>'
                    array.append(output_str)
                else:
                    output_str = row[i + 3]
                    array.append(output_str)
            elif row[i] == value and value == 'Template':
                if str(row[i + 3]) == 'nan':
                    output_str = '<placeholder>'
                    array.append(output_str)
                else:
                    input_str = row[i + 3]
                    output_str = re.sub(r'\$\((\w+)\)', r'${\1}', input_str)
                    output_str = output_str.replace('"${', '${').replace('}"', '}').replace("\n", "")
                    array.append(output_str)
            i += 1
    return array

def dynamic_values_array_of_arrays(template_array):
    dynamic_values_array_of_arrays = []

    i = 0
    while i < len(template_array):
        dynamic_values_list = []
        entry = template_array[i].split('${')
        for lines in entry:
            lines = lines.split('}')
            for value in lines:
                if len(value.split()) == 1 and re.search("^[A-Za-z0-9_]+$", value):
                    dynamic_values_list.append(value)
        dynamic_values_list = list(set(dynamic_values_list))
        dynamic_values_array_of_arrays.append(dynamic_values_list)
        i += 1
    return dynamic_values_array_of_arrays

def query_template_entry(i, template, template_id, app_name, template_regex):
    if template != "<placeholder>" and template != 'nric_uuid_template' and template != 'uuid_nric_template':
        yaml_entry = f'''

# {i + 1}
-   pkstatus: true
    dataSource: hasura
    querytemplate: '{template}'
    pk: {template_id}
    appid: {app_name}
    paramValuesSchema:'''

        if template_regex == []:
            required = '''
    required: []'''
            yaml_entry += required

        else:
            for pair in template_regex:
                pair_portion = f'''
        {pair}:
            pattern:
            type:'''
                yaml_entry += pair_portion

            required = '''
    required:'''
            yaml_entry += required

            for pair in template_regex:
                value_portion = f'''
            - {pair}'''
                yaml_entry += value_portion
    
    else:
        yaml_entry = ''
    
    return yaml_entry

def mds_query_template_yaml(template_array, template_id_array, app_name, template_regex_array):
    yaml_file = '''---'''
    i = 0
    while i < len(template_array):
        if template_array[i] != '<placeholder>':
            yaml_entry = query_template_entry(i, template_array[i], template_id_array[i], app_name, template_regex_array[i])
            yaml_file += yaml_entry
            i += 1
        else:
            yaml_file += ''
            i += 1

    if yaml_file == '''---''':
        return 0
    else:
        return yaml_file

# MDS Data Contract
def column_array(df, value):
    start_index = []
    column = []
    end_index = []
    for index, row in df.iterrows():
        i = 0
        while i < len(df.columns):
            if row[i] == value:
                start_index.append(index + 1)
                column.append(i)
            elif row[i] == '<Add more entries here if necessary>':
                end_index.append(index)
            i += 1
    column_array = []
    for item in df.iloc[start_index[0]:end_index[0], column[0]]:
        column_array.append(item)
    column_array = list(map(lambda x: str(x).lower(), column_array))
    return column_array

def table_names(array):
    remove_nan = [x for x in array if str(x) != 'nan']
    table_names = []
    for name in remove_nan:
        if name == 'audit_code' or name == 'audit_infotype' or name == 'nric_uuid_main' or name == 'it_main':
            table_names.append(name)
        elif name.split('_')[0] == 'cd':
            name = name.replace('_', '')
            table_names.append(name + '_main')
        else:
            table_names.append(name + '_main')
    return table_names

def field_array_of_arrays(ref_array, split_array):
    field_array_of_arrays = []
    array = []
    i = 0
    while i < len(split_array):
        if i == 0:
            array.append(split_array[i])
        elif ref_array[i] == 'nan' and ref_array[i - 1] == 'nan' or ref_array[i] == 'nan' and ref_array[i - 1] != 'nan':
            array.append(split_array[i])
        else:
            field_array_of_arrays.append(array)
            array = []
            array.append(split_array[i])
        i += 1
    field_array_of_arrays.append(array)
    return field_array_of_arrays

def data_contract_yaml(app_name, table_names_array, field_array_of_arrays):
    yaml_file = f'''---
role: [{app_name}]
filter: {{
    it0001_persg: [], # e.g [A,B,C]
    it0001_werks: []  # e.g ["0001","0002","0003"]
}}

table:'''

    i = 0
    while i < len(table_names_array):
        field_array_of_arrays[i] = list(filter(lambda x: x != 'nan', field_array_of_arrays[i]))
        field_array_of_arrays[i] = str(field_array_of_arrays[i]).replace("'", '')
        yaml_entry = f'''
-   tablename: {table_names_array[i]}
    columns: {field_array_of_arrays[i]}
    limit: null
    allow_aggregations: false
'''
        yaml_file += yaml_entry
        i += 1
    
    if yaml_file == f'''---
role: [{app_name}]
filter: {{
    it0001_persg: [], # e.g [A,B,C]
    it0001_werks: []  # e.g ["0001","0002","0003"]
}}

table:''':
        return 0
    else:
        return yaml_file
