import re

def mcns_authorizer_entry(app_name, template_id, channel_type, sender, subject, template, dynamic_value_array, regex_json, env):
    if template == 'nan':
        return ''

    required = str(dynamic_value_array).replace("'", '\\"').replace("[", "").replace("]", "")
    properties = []
    for value in dynamic_value_array:
        output_str = f'\\"{value}\\":{{\\"description\\":\\"{value}field\\", \\"type\\":\\"string\\"}}'
        properties.append(output_str)
    properties = str(properties)[1:-1]
    properties = str(properties).replace("'", '').replace("[", "").replace("]", "").replace('\\"','\"')

    if channel_type == 'email':
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        valid_email = re.findall(email_pattern, sender)
        if valid_email ==  [] and env == 'sit':
            sender = sender + '@sit.df-mcns.com'
        elif valid_email == [] and env == 'prod':
            sender = sender + '@mcns.defence.gov.sg'
        sender = sender.lower()
        
    if channel_type == 'sms':
        if env == 'sit' and sender == 'nan':
            sender = '+6580283091'
        elif env == 'prod' and sender == 'nan':
            sender = 'MINDEF'
        subject = 'MCNS Notification'

    mcns_authorizer_entry = f'''
        {{
            "PutRequest": {{
                "Item": {{
                    "pk": {{
                        "S": "{app_name}#{sender}#{template_id}"
                    }},
                    "subject": {{
                        "S": "{subject}"
                    }}'''
    if dynamic_value_array != []:
        template_value_schema = f''',
                    "templateValueSchema": {{
                        "S": "{{\\"$schema\\":\\"https://json-schema.org/draft/2020-12/schema\\",\\"$id\\":\\"https://dsta.gov.sg/app1.schema.json\\",\\"title\\":\\"app1\\",\\"type\\":\\"object\\",\\"properties\\":{{{properties}}},\\"required\\":[{required}]}}"
                    }}'''
        mcns_authorizer_entry += template_value_schema
    mcns_authorizer_entry += f''',
                    "template": {{
                        "S": "{template}"
                    }}'''
    if "templateValueSchema" in mcns_authorizer_entry:
        regex_schema = f''',
                    "regEx": {{
                        "S": "{regex_json}"
                    }}'''
        mcns_authorizer_entry += regex_schema
    mcns_authorizer_entry += ''',
                    "pkstatus": {
                        "S": "true"
                    }'''
    if channel_type == 'email':
        attachment_allowed = ''',
                    "attachmentAllowed": {
                        "S": "true"
                    }'''
        mcns_authorizer_entry += attachment_allowed
    mcns_authorizer_entry += '''
                }
            }
        },'''
    return mcns_authorizer_entry

def mcns_authorizer_content(app_name, template_id_array, channel_type_array, sender_array, subject_array, template_array, dynamic_value_arrays, regex_json_array, env):
    content = f'''{{
    "mcns-authorizer-{env}": [ '''
    content_footer = '''
    ]
}'''

    i = 0
    while i < len(template_array):
        if template_array[i] != 'nan':
            auth_entry = mcns_authorizer_entry(app_name, template_id_array[i], channel_type_array[i], sender_array[i], subject_array[i], template_array[i], dynamic_value_arrays[i], regex_json_array[i], env)
            content += auth_entry
        i += 1

    content = content[:-1]
    content += content_footer

    if content != f'''{{
    "mcns-authorizer-{env}": [
    ]
}}''':
        return content
    return None