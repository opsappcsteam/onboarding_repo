import pandas as pd
import shared_functions as sf
import sft_functions as sfs

def sft_onboarding(env):
  app_name = sf.get_excel_name()
  excelsheet_info = pd.read_excel(sf.get_excel_path(), 'SFT')

  sns_callback_array = sfs.sft_array(excelsheet_info, 'SNS')
  http_callback_array = sfs.sft_array(excelsheet_info, 'HTTP')
  file_type_array = list(set(sfs.sft_array(excelsheet_info, 'File Type')))
  file_type_array = list(filter(lambda x: x != '(Select)', file_type_array))

  sft_authorizer_content = sfs.sft_auth_json(app_name, file_type_array, sns_callback_array, http_callback_array, env)
  sft_auth_json = sf.file_generation(app_name, 'sft_authorizer', sft_authorizer_content, '.json')
