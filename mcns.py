import pandas as pd
import shared_functions as sf
import mcns_functions as mf

def mcns_onboarding(env):
  app_name = sf.get_excel_name()
  excelsheet_info = pd.read_excel(sf.get_excel_path(), 'MCNS')

  template_id_array = mf.mcns_array(excelsheet_info, 'Template ID')
  channel_type_array = mf.mcns_array(excelsheet_info, 'Channel Type')
  sender_array = mf.mcns_array(excelsheet_info, 'Sender')
  subject_array = mf.mcns_array(excelsheet_info, 'Subject')
  template_array = mf.mcns_array(excelsheet_info, 'Template')
  dynamic_values_array = sf.dynamic_values_array(subject_array, template_array)
  template_regex_array = mf.mcns_array(excelsheet_info, "Template Values' Regular Expression")

  mcns_auth_content = mf.mcns_auth_json(app_name, template_id_array, channel_type_array, sender_array, subject_array, template_array, dynamic_values_array, template_regex_array, 'prod')
  mcns_config_content = mf.mcns_config_json(app_name, template_id_array, sender_array, channel_type_array, env)

  mcns_auth_json = sf.file_generation(app_name, 'mcns_authorizer', mcns_auth_content, '.json')
  mcns_config_json = sf.file_generation(app_name, 'mcns_configuration', mcns_config_content, '.json')
