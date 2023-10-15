import pandas as pd
from services.common.arrays import *
from services.common.array_manipulation import *
from services.common.file_generation import *
from .mcns_auth import *
from .mcns_config import *
from .mcns_service import *

def mcns_onboard(excel_path, app_name, env):
    mcns_sheet = pd.read_excel(excel_path, 'MCNS')
    channel_type_array = channel_type_converter(row_array(mcns_sheet, 'Channel Type', 2))
    template_id_array = template_id_converter(uuid_generator(row_array(mcns_sheet, 'Template ID', 2)), channel_type_array)
    sender_array = row_array(mcns_sheet, 'Sender', 2)
    subject_array = template_subject_cleaner(row_array(mcns_sheet, 'Subject', 2), 'MCNS')
    template_array = template_subject_cleaner(row_array(mcns_sheet, 'Template', 2), 'MCNS')
    regex_array = dynamic_values_array_generator(subject_array, template_array)
    regex_json_array = regex_json_converter(row_array(mcns_sheet, "Template Values' Regular Expression", 2))
    
    authorizer_content = mcns_authorizer_content(app_name, template_id_array, channel_type_array, sender_array, subject_array, template_array, regex_array, regex_json_array, env)
    configuration_content = mcns_configuration_content(app_name, template_id_array, channel_type_array, sender_array, template_array, env)

    onboarding_file_generation(app_name, 'MCNS', 'Authorizer', authorizer_content, '.json', '')
    onboarding_file_generation(app_name, 'MCNS', 'Configuration', configuration_content, '.json', '')

def mcns_report(excel_path, app_name, env):
    mcns_sheet = pd.read_excel(excel_path, 'MCNS')
    channel_type_array = channel_type_converter(row_array(mcns_sheet, 'Channel Type', 2))
    template_id_array = template_id_converter(uuid_generator(row_array(mcns_sheet, 'Template ID', 2)), channel_type_array)
    sender_array = row_array(mcns_sheet, 'Sender', 2)
    subject_array = template_subject_cleaner(row_array(mcns_sheet, 'Subject', 2), 'MCNS')
    template_array = template_subject_cleaner(row_array(mcns_sheet, 'Template', 2), 'MCNS')
    regex_array = dynamic_values_array_generator(subject_array, template_array)
    regex_json_array = regex_validator(row_array(mcns_sheet, "Template Values' Regular Expression", 2))

    invalid_json_array = invalid_regex_identifier(regex_json_array)
    most_common_length = most_common_length_getter([len(channel_type_array), len(template_id_array), len(sender_id_array), len(subject_array), len(template_array), len(regex_json_array)])
    
    array_name_length_dictionary = { 'channel type array': len(channel_type_array), 'template id array': len(template_id_array), 'sender array': len(sender_array), 'subject array': len(subject_array), 'template array': len(template_array), 'regex json array': len(regex_json_array)}
    missing_row_array = []
    for key, value in array_name_length_dictionary.items():
        if value != most_common_length:
            missing_row_array.append(key)
    
    if invalid_json_array == [] and missing_row_array == []:
        print('''MCNS:
- Missing Row: None
- Regex JSON Invalidation: None''')
    else:
        print(f'''MCNS:
- Missing Row: {missing_row_array}
- Regex JSON Invalidation: {invalid_json_array}'''
    
