import re

def mcns_array(df, value, env):
    array = []
    for index, row in df.iterrows():
        i = 0
        while i < len(df.columns):
            if row[i] == value and value == 'Template ID':
                if row[i + 2] == '<This will be filled up by AppCS Onboarding Team>' or str(row[i + 2]) == 'nan':
                    output_str = '<placeholder>'
                    array.append(output_str)
                else:
                    output_str = row[i + 2]
                    array.append(output_str)
            elif row[i] == value and value == 'Channel Type':
                if row[i + 2] == '(Select)' or str(row[i + 2]) == 'nan':
                    output_str = '<placeholder>'
                    array.append(output_str)
                else:
                    output_str = row[i + 2]
                    array.append(output_str)
            elif row[i] == value and value == 'Sender':
                if env == 'sit':
                    if str(row[i + 2]) == 'nan':
                        output_str = '<placeholder>'
                        array.append(output_str)
                    else:
                        output_str = row[i + 2]
                        if '@sit.df-mcns.com' in output_str:
                            array.append(output_str)
                        else:
                            output_str = row[i + 2].lower() + '@sit.df-mcns.com'
                            array.append(output_str)
                elif env == 'prod':
                    if str(row[i + 2]) == 'nan':
                        output_str = '<placeholder>'
                        array.append(output_str)
                    else:
                        output_str = row[i + 2]
                        if '@mcns.defence.gov.sg' in output_str:
                            array.append(output_str)
                        else:
                            output_str = row[i + 2].lower() + '@mcns.defence.gov.sg'
                            array.append(output_str)
            elif row[i] == value and value == 'Subject':
                if str(row[i + 2]) == 'nan':
                    output_str = '<placeholder>'
                    array.append(output_str)
                else:
                    input_str = row[i + 2]
                    output_str = re.sub(r'\$\((\w+)\)', r'${\1}', input_str)
                    output_str = output_str.replace('"${', '${').replace('}"', '}')
                    array.append(output_str)
            elif row[i] == value and value == 'Template':
                if str(row[i + 2]) == 'nan':
                    output_str = '<placeholder>'
                    array.append(output_str)
                else:
                    input_str = row[i + 2]
                    output_str = re.sub(r'\$\((\w+)\)', r'${\1}', input_str)
                    output_str = output_str.replace('"${', '${').replace('}"', '}').split("\n")
                    output_str = ' '.join(line.lstrip() for line in output_str)
                    output_str = output_str.replace('\t', '    ')
                    output_str = output_str.replace("'", '"').replace(r'"', r'\"')
                    array.append(output_str)
            elif row[i] == value and value == "Template Values' Regular Expression":
                if str(row[i + 2]) == 'nan':
                    item = '<placeholder>'
                    array.append(item)
                else:
                    item = row[i + 2].replace('\\', '\\\\\\\\').replace("\n", "").replace('"', '\\"').replace('   ', '')
                    array.append(item)
            i += 1
    return array

def mcns_auth_entry(app_name, template_id, channel_type, sender, subject, template, dynamic_values, regex_json):
    channel_type = channel_type.lower()
    if template_id == '<placeholder>':
        template_id = channel_type.lower() + '<uuid>'
    if regex_json == '<placeholder>':
        regex_json = ''
    
    required = str(dynamic_values).replace("'", '\\"').replace("[", "").replace("]", "")
    properties = []
    for value in dynamic_values:
        output_str = f'\\"{value}\\":{{\\"description\\":\\"{value}field\\", \\"type\\":\\"string\\"}}'
        properties.append(output_str)
    properties = str(properties)[1:-1]
    properties = str(properties).replace("'", '').replace("[", "").replace("]", "").replace('\\"','\"')

    if channel_type == 'email' and regex_json != '':
        mcns_auth_entry = f'''
        {{
            "PutRequest": {{
                "Item": {{
                    "pk": {{
                        "S": "{app_name}#{sender}#{template_id}"
                    }},
                    "subject": {{
                        "S": "{subject}"
                    }},
                    "templateValueSchema": {{
                        "S": "{{\\"$schema\\":\\"https://json-schema.org/draft/2020-12/schema\\",\\"$id\\":\\"https://dsta.gov.sg/app1.schema.json\\",\\"title\\":\\"app1\\",\\"type\\":\\"object\\",\\"properties\\":{{{properties}}},\\"required\\":[{required}]}}"
                    }},
                    "template": {{
                        "S": "{template}"
                    }},
                    "regEx": {{
                        "S": "{regex_json}"
                    }},
                    "pkstatus": {{
                        "S": "true"
                    }},
                     "attachmentAllowed": {{
                        "S": "true"
                    }}
                }}
            }}
        }}'''
    elif channel_type == 'email' and regex_json == '':
        mcns_auth_entry = f'''
        {{
            "PutRequest": {{
                "Item": {{
                    "pk": {{
                        "S": "{app_name}#{sender}#{template_id}"
                    }},
                    "subject": {{
                        "S": "{subject}"
                    }},
                    "template": {{
                        "S": "{template}"
                    }},
                    "pkstatus": {{
                        "S": "true"
                    }},
                     "attachmentAllowed": {{
                        "S": "true"
                    }}
                }}
            }}
        }}'''
    elif channel_type == 'sms' and regex_json != '':
        mcns_auth_entry = f'''
        {{
            "PutRequest": {{
                "Item": {{
                    "pk": {{
                        "S": "{app_name}#{sender}#{template_id}"
                    }},
                    "subject": {{
                        "S": "MCNS Notification"
                    }},
                    "templateValueSchema": {{
                        "S": "{{\\"$schema\\":\\"https://json-schema.org/draft/2020-12/schema\\",\\"$id\\":\\"https://dsta.gov.sg/app1.schema.json\\",\\"title\\":\\"app1\\",\\"type\\":\\"object\\",\\"properties\\":{{{properties}}},\\"required\\":[{required}]}}"
                    }},
                    "template": {{
                        "S": "{template}"
                    }},
                    "regEx": {{
                        "S": "{regex_json}"
                    }},
                    "pkstatus": {{
                        "S": "true"
                    }}
                }}
            }}
        }}'''
    elif channel_type == 'sms' and regex_json == '':
        mcns_auth_entry = f'''
        {{
            "PutRequest": {{
                "Item": {{
                    "pk": {{
                        "S": "{app_name}#{sender}#{template_id}"
                    }},
                    "subject": {{
                        "S": "MCNS Notification"
                    }},
                    "template": {{
                        "S": "{template}"
                    }},
                    "pkstatus": {{
                        "S": "true"
                    }}
                }}
            }}
        }}'''
    elif channel_type == 'push' and regex_json != '':
        mcns_auth_entry = f'''
        {{
            "PutRequest": {{
                "Item": {{
                    "pk": {{
                        "S": "{app_name}#{sender}#{template_id}"
                    }},
                    "subject": {{
                        "S": "{subject}"
                    }},
                    "templateValueSchema": {{
                        "S": "{{\\"$schema\\":\\"https://json-schema.org/draft/2020-12/schema\\",\\"$id\\":\\"https://dsta.gov.sg/app1.schema.json\\",\\"title\\":\\"app1\\",\\"type\\":\\"object\\",\\"properties\\":{{{properties}}},\\"required\\":[{required}]}}"
                    }},
                    "template": {{
                        "S": "{template}"
                    }},
                    "regEx": {{
                        "S": "{regex_json}"
                    }},
                    "pkstatus": {{
                        "S": "true"
                    }}
                }}
            }}
        }}'''
    elif channel_type == 'push' and regex_json == '':
        mcns_auth_entry = f'''
        {{
            "PutRequest": {{
                "Item": {{
                    "pk": {{
                        "S": "{app_name}#{sender}#{template_id}"
                    }},
                    "subject": {{
                        "S": "{subject}"
                    }},
                    "template": {{
                        "S": "{template}"
                    }},
                    "pkstatus": {{
                        "S": "true"
                    }}
                }}
            }}
        }}'''
    else:
        mcns_auth_entry = ''
    return mcns_auth_entry

def mcns_auth_json(app_name, template_id_array, channel_type_array, sender_array, subject_array, template_array, dynamic_values_array, template_regex_array, env):
    json_file = f'''{{
    "mcns-authorizer-{env}": ['''
    json_footer = '''
    ]
}'''
    i = 0
    while i < len(template_array):
        if template_array[i] != '<placeholder>':
            if i != len(template_array) - 1: 
                json_auth_entry = mcns_auth_entry(app_name, template_id_array[i], channel_type_array[i], sender_array[i], subject_array[i], template_array[i], dynamic_values_array[i], template_regex_array[i])
                json_file += json_auth_entry + ','
            else:
                json_auth_entry = mcns_auth_entry(app_name, template_id_array[i], channel_type_array[i], sender_array[i], subject_array[i], template_array[i], dynamic_values_array[i], template_regex_array[i])
                json_file += json_auth_entry
            i += 1
        else:
            json_file += ''
            i += 1
    json_file += json_footer

    mcns_blank_authorizer_content = f'''{{
    "mcns-authorizer-{env}": [
    ]
}}'''

    if json_file == mcns_blank_authorizer_content:
        return 0
    else:
        return json_file

def mcns_config_entry(app_name, template_id, sender, channel_type):
    channel_type = channel_type.lower()
    if template_id == '<placeholder>':
        template_id = channel_type.lower() + '<uuid>'
    if channel_type == 'email':
        mcns_config_entry = f'''
        {{
            "PutRequest": {{
                "Item": {{
                    "pk": {{
                        "S": "{app_name}#{sender}#{template_id}"
                    }},
                    "sk": {{
                        "S": "email"
                    }},
                    "appid": {{
                        "S": "<placeholder>"
                    }}
                }}
            }}
        }}'''
    elif channel_type == 'sms':
        mcns_config_entry = f'''
        {{
            "PutRequest": {{
                "Item": {{
                    "pk": {{
                        "S": "{app_name}#{sender}#{template_id}"
                    }},
                    "sk": {{
                        "S": "sms"
                    }},
                    "appid": {{
                        "S": "<placeholder>"
                    }},
                    "originationNumber": {{
                        "S": "73884"
                    }}
                }}
            }}
        }}'''
    elif channel_type == 'push':
        mcns_config_entry = f'''
        {{
            "PutRequest": {{
                "Item": {{
                    "pk": {{
                        "S": "{app_name}#{sender}#{template_id}"
                    }},
                    "sk": {{
                        "S": "push"
                    }},
                    "appid": {{
                        "S": "<placeholder>"
                    }}
                }}
            }}
        }}'''
    else:
        mcns_config_entry = ''

    return mcns_config_entry

def mcns_config_json(app_name, template_id_array, sender_array, channel_type_array, env):
    json_file = f'''{{
    "mcns-configuration-{env}": ['''
    json_footer = '''
    ]
}'''

    i = 0
    while i < len(channel_type_array):
        if channel_type_array[i] != '<placeholder>':
            if i != len(channel_type_array) - 1: 
                json_config_entry = mcns_config_entry(app_name, template_id_array[i], sender_array[i], channel_type_array[i])
                json_file += json_config_entry + ','
            else:
                json_config_entry = mcns_config_entry(app_name, template_id_array[i], sender_array[i], channel_type_array[i])
                json_file += json_config_entry
            i += 1
        else:
            json_file += ''
            i += 1
    json_file += json_footer

    mcns_blank_configuration_content = f'''{{
    "mcns-configuration-{env}": [
    ]
}}'''

    if json_file == mcns_blank_configuration_content:
        return 0
    else:
        return json_file
