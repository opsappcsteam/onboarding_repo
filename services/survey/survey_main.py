import pandas as pd
from services.common.arrays import *
from .survey_service import *

def survey_main(excel_path, app_name):
    survey_info = pd.read_excel(excel_path, 'Survey')
    operation_array = column_array(survey_info, 'Action')
    role_array = column_array(survey_info, 'Role')
    email_array = column_array(survey_info, 'Official Email')
    onboard_csv_content(operation_array, app_name, role_array, email_array)
    reset_csv_content(operation_array, app_name, role_array, email_array)
    unlock_csv_content(operation_array, app_name, role_array, email_array)