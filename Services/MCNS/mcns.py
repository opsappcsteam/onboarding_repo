import pandas as pd
import Services.shared_functions as sf
import Services.MCNS.mcns_functions as mf

def mcns_onboarding(env):
  app_name = sf.get_excel_name()
  excelsheet_info = pd.read_excel(sf.get_excel_path(), 'MCNS')

  template_id_array = mf.mcns_array(excelsheet_info, 'Template ID', env)
  channel_type_array = mf.mcns_array(excelsheet_info, 'Channel Type', env)
  sender_array = mf.mcns_array(excelsheet_info, 'Sender', env)
  subject_array = mf.mcns_array(excelsheet_info, 'Subject', env)
  template_array = mf.mcns_array(excelsheet_info, 'Template', env)
  dynamic_values_array = sf.dynamic_values_array(subject_array, template_array)
  template_regex_array = mf.mcns_array(excelsheet_info, "Template Values' Regular Expression", env)

  mcns_auth_content = mf.mcns_auth_json(app_name, template_id_array, channel_type_array, sender_array, subject_array, template_array, dynamic_values_array, template_regex_array, env)
  mcns_config_content = mf.mcns_config_json(app_name, template_id_array, sender_array, channel_type_array, env)

  mcns_auth_json = sf.file_generation(app_name, 'mcns_authorizer', mcns_auth_content, '.json')
  mcns_config_json = sf.file_generation(app_name, 'mcns_configuration', mcns_config_content, '.json')
