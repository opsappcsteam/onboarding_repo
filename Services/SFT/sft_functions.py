def sft_array(df, value):
    array = []
    for index, row in df.iterrows():
        i = 0
        while i < len(df.columns):
            if row[i] == value and value == 'SNS':
                if str(row[i + 2]) == 'nan':
                    output_str = '<placeholder>'
                    array.append(output_str)
                else:
                    output_str = row[i + 2]
                    array.append(output_str)
            elif row[i] == value and value == 'HTTP':
                if str(row[i + 2]) == 'nan':
                    output_str = '<placeholder>'
                    array.append(output_str)
                else:
                    output_str = row[i + 2]
                    array.append(output_str)
            elif row[i] == value and value == 'File Type':
                if row[i + 1] == '(Select)' or str(row[i + 1]) == 'nan':
                    pass
                elif row[i + 1] == 'image/jpg (.jpg)':
                    output_str = 'image/jpeg'
                    array.append(output_str)
                else:
                    output_str = row[i + 1]
                    output_str = output_str.split(' ')[0]
                    array.append(output_str)
            i += 1
    return array

def sft_entry(app_name, file_type, sns_callback, http_callback):
    if file_type == '<placeholder>':
        sft_entry = ''
    elif sns_callback == '<placeholder>' and http_callback == '<placeholder>':
        sft_entry = f'''
        {{
            "PutRequest": {{
                "Item": {{
                    "pk": {{
                        "S": "{app_name}#{file_type}"
                    }},
                    "pkstatus": {{
                        "S": "true"
                    }}
                }}
            }}
        }}'''
    elif sns_callback == '<placeholder>' and http_callback != '<placeholder>':
        sft_entry = f'''
        {{
            "PutRequest": {{
                "Item": {{
                    "pk": {{
                        "S": "{app_name}#{file_type}"
                    }},
                    "pkstatus": {{
                        "S": "true"
                    }},
                    "httpCallback": {{
                        "S": "{http_callback}"
                    }}
                }}
            }}
        }}'''
    elif http_callback == '<placeholder>' and sns_callback != '<placeholder>':
        sft_entry = f'''
        {{
            "PutRequest": {{
                "Item": {{
                    "pk": {{
                        "S": "{app_name}#{file_type}"
                    }},
                    "pkstatus": {{
                        "S": "true"
                    }},
                    "callback": {{
                        "S": "{sns_callback}"
                    }}
                }}
            }}
        }}'''
    else:
        sft_entry = f'''
        {{
            "PutRequest": {{
                "Item": {{
                    "pk": {{
                        "S": "{app_name}#{file_type}"
                    }},
                    "pkstatus": {{
                        "S": "true"
                    }},
                    "httpCallback": {{
                        "S": "{http_callback}"
                    }},
                    "callback": {{
                        "S": "{sns_callback}"
                    }}
                }}
            }}
        }}'''
    return sft_entry

def sft_auth_json(app_name, file_type_array, http_callback_array, sns_callback_array, env):
    sft_file = f'''{{
    "sft-authorizer-{env}": ['''
    sft_footer = '''
    ]
}'''
    if len(file_type_array) == 0:
        sft_file += sft_footer
    else:
        if len(http_callback_array) == 0:
            http_callback_array = ['<placeholder>']
        if len(sns_callback_array) == 0:
            sns_callback_array = ['<placeholder>']
        i = 0
        while i < len(file_type_array):
            if i == len(file_type_array) - 1:
                sft_file += sft_entry(app_name, file_type_array[i], http_callback_array[0], sns_callback_array[0])
            else:
                sft_file += sft_entry(app_name, file_type_array[i], http_callback_array[0], sns_callback_array[0]) + ','
            i += 1
        sft_file += sft_footer

    if sft_file == f'''{{
    "sft-authorizer-{env}": [
    ]
}}''':
        return 0
    else:
        return sft_file
