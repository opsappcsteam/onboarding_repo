import pandas as pd
from services.common.arrays import *
from services.common.excelsheet import *
from services.common.file_generation import *
from services.common.array_manipulation import *
from .sft_auth import *
from .sft_service import *

def sft_main(excel_path, app_name, env):
    sft_sheet = pd.read_excel(excel_path, 'SFT')
    sns_callback = nan_remover(row_array(sft_sheet, 'SNS', 2))
    http_callback = nan_remover(row_array(sft_sheet, 'HTTP', 2))
    clean_file_type_array_v1 = file_type_cleaner(row_array(sft_sheet, 'File Type', 1))
    clean_file_type_array_v2 = file_type_cleaner(row_array(sft_sheet, True, 1))
    sft_content_v1 = sft_authorizer_content(app_name, sns_callback, http_callback, clean_file_type_array_v1, env)
    sft_content_v2 = sft_authorizer_content(app_name, sns_callback, http_callback, clean_file_type_array_v2, env)
    onboarding_file_generation(app_name, 'SFT', 'Authorizer', sft_content_v1, '.json', 'v1')
    onboarding_file_generation(app_name, 'SFT', 'Authorizer', sft_content_v2, '.json', 'v2')