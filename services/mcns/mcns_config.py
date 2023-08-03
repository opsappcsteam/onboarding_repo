import re

def mcns_configuration_entry(app_name, template_id, channel_type, sender, env):

    origination_number = ''

    if channel_type == 'email':
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        valid_email = re.findall(email_pattern, sender)
        if valid_email ==  [] and env == 'sit':
            sender = sender + '@sit.df-mcns.com'
            sender = sender.lower()
        elif valid_email != [] and env == 'sit':
            sender = sender.lower()
        elif valid_email == [] and env == 'prod':
            sender = sender + '@mcns.defence.gov.sg'

    if channel_type == 'sms':
        if env == 'sit' and sender != 'nan':
            sender = sender.lower()
            origination_number = '+6580283091'
        elif env == 'prod' and sender != 'nan':
            origination_number = '73884'
        elif env == 'sit' and sender == 'nan':
            sender = '+6580283091'
            origination_number = '+6580283091'
        elif env == 'prod' and sender == 'nan':
            sender = 'MINDEF'
            origination_number = '73884'

    if channel_type == 'push' and env == 'sit':
        sender = sender.lower()

    mcns_config_entry = f'''
        {{
            "PutRequest": {{
                "Item": {{
                    "pk": {{
                        "S": "{app_name}#{sender}#{template_id}"
                    }},
                    "sk": {{
                        "S": "{channel_type}"
                    }},
                    "appid": {{
                        "S": "<placeholder>"
                    }}'''
    if channel_type == 'sms':
        origination_number_json = f''',
                    "originationNumber": {{
                        "S": "{origination_number}"
                    }}'''
        mcns_config_entry += origination_number_json
    mcns_config_footer = f'''
                }}
            }}
        }},'''
    mcns_config_entry += mcns_config_footer
    return mcns_config_entry

def mcns_configuration_content(app_name, template_id_array, channel_type_array, sender_array, template_array, env):
    content = f'''{{
    "mcns-configuration-{env}": [ '''
    content_footer = '''
    ]
}'''

    i = 0
    while i < len(template_array):
        if template_array[i] != 'nan':
            config_entry = mcns_configuration_entry(app_name, template_id_array[i], channel_type_array[i], sender_array[i], env)
            content += config_entry
        i += 1

    content = content[:-1]
    content += content_footer

    if content != f'''{{
    "mcns-configuration-{env}": [
    ]
}}''':
        return content
    return None
