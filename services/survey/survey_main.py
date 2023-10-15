import pandas as pd
from services.common.arrays import *
from services.common.file_generation import *
from .survey_service import *

def survey_onboard(excel_path, app_name):
    survey_info = pd.read_excel(excel_path, 'Survey')
    operation_array = column_array(survey_info, 'Action')
    role_array = column_array(survey_info, 'Role')
    email_array = column_array(survey_info, 'Official Email')
    onboard_content = onboard_csv_content(operation_array, app_name, role_array, email_array)
    reset_content = reset_csv_content(operation_array, app_name, role_array, email_array)
    unlock_content = unlock_csv_content(operation_array, app_name, role_array, email_array)

    onboarding_file_generation(app_name, 'Survey', 'Onboard', onboard_content, '.csv', '')
    onboarding_file_generation(app_name, 'Survey', 'Reset', reset_content, '.csv', '')
    onboarding_file_generation(app_name, 'Survey', 'Unlock', unlock_content, '.csv', '')
