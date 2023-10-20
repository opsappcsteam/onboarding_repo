import pandas as pd
from services.common.arrays import *
from services.common.array_manipulation import *
from services.common.file_generation import *
from .mcns_auth import *
from .mcns_config import *
from .mcns_service import *

def mcns_main(excel_path, app_name, env):
    mcns_sheet = pd.read_excel(excel_path, 'MCNS', keep_default_na=False)
    channel_type_array = channel_type_converter(row_array(mcns_sheet, 'Channel Type', 2))
    template_id_array = template_id_converter(uuid_generator(row_array(mcns_sheet, 'Template ID', 2)), channel_type_array)
    sender_array = row_array(mcns_sheet, 'Sender', 2)
    subject_array = subject_cleaner(row_array(mcns_sheet, 'Subject', 2), 'MCNS')
    template_array = template_cleaner(row_array(mcns_sheet, 'Template', 2), 'MCNS', channel_type_array)
    regex_array = dynamic_values_array_generator(subject_array, template_array)
    regex_json_array = regex_json_converter(row_array(mcns_sheet, "Template Values' Regular Expression", 2))
    
    authorizer_content = mcns_authorizer_content(app_name, template_id_array, channel_type_array, sender_array, subject_array, template_array, regex_array, regex_json_array, env)
    configuration_content = mcns_configuration_content(app_name, template_id_array, channel_type_array, sender_array, template_array, env)

    onboarding_file_generation(app_name, 'MCNS', 'Authorizer', authorizer_content, '.json', '')
    onboarding_file_generation(app_name, 'MCNS', 'Configuration', configuration_content, '.json', '')
