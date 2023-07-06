def mds_template_entry(app_name, template, template_id, dynamic_value_array, i):
    if template_id == 'nric_uuid_template' or template_id == 'uuid_nric_template' or template == 'nan':
        template_entry = ''
    else:
        template_entry = f'''

# {i + 1}
-   pkstatus: true
    dataSource: hasura
    querytemplate: '{template}'
    pk: {template_id}
    appid: {app_name}
    paramValuesSchema:'''
        if dynamic_value_array == []:
            required = '''
    required: []'''
            template_entry += required
        else:
            for value in dynamic_value_array:
                paramValues_entry = f'''
        {value}:
            pattern:
            type:'''
                template_entry += paramValues_entry
            required = '''
    required:'''
            template_entry += required
            for value in dynamic_value_array:
                required_value = f'''
        - {value}'''
                template_entry += required_value
    return template_entry

def mds_template_content(app_name, template_array, template_id_array, dynamic_value_arrays):
    content = '---'

    i = 0
    while i < len(template_array):
        content += mds_template_entry(app_name, template_array[i], template_id_array[i], dynamic_value_arrays[i], i)
        i += 1
    if content != '---':
        return content
    return None