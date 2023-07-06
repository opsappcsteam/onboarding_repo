from services.common.excelsheet import *

def sft_authorizer_entry(app_name, sns_callback, http_callback, file_type):
    entry = f'''
        {{
            "PutRequest": {{
                "Item": {{
                    "pk": {{
                        "S": "{app_name}#{file_type}"
                    }},
                    "pkstatus": {{
                        "S": "true"
                    }}'''
    if http_callback != []:
        entry += f''',
                    "httpCallback": {{
                        "S": "{http_callback[0]}"
                    }}'''
    if sns_callback != []:
        entry += f''',
                    "callback": {{
                        "S": "{sns_callback[0]}"
                    }}'''
    entry_end = '''
                }
            }
        },'''
    entry += entry_end
    return entry

def sft_authorizer_content(app_name, sns_callback, http_callback, file_type_array, env):
    content = f'''{{
    "sft-authorizer-{env}": [ '''
    content_footer = '''
    ]
}'''
    for file_type in file_type_array:
        content += sft_authorizer_entry(app_name, sns_callback, http_callback, file_type)

    content = content[:-1]
    content += content_footer

    if content != f'''{{
    "sft-authorizer-{env}": [
    ]
}}''':
        return content
    return None