import pandas as pd
from services.common.array_manipulation import *
from services.common.arrays import *
from services.common.file_generation import *
from .mds_contract import *
from .mds_template import *
from .mds_service import *

def mpds_main(excel_path, app_name):
    mpds_sheet = pd.read_excel(excel_path, 'MPDS')
    pop_svc_array = pop_svc_converter(row_array(mpds_sheet, True, 1))
    table_name_array = main_name_converter(nan_remover(column_array(mpds_sheet, 'Table Name')))
    field_arrays = nan_remover(field_array_splitter(column_array(mpds_sheet, 'Table Name'), column_array(mpds_sheet, 'Field')))
    mpds_data_contract_content = mds_contract_content(app_name, pop_svc_array, table_name_array, field_arrays)

    template_id_array = row_array(mpds_sheet, 'Template ID', 3)
    template_array = template_subject_cleaner(row_array(mpds_sheet, 'Template', 3), 'MPDS')
    regex_arrays = dynamic_values_array_generator([], template_array)
    mpds_query_template_content = mds_template_content(app_name, template_array, template_id_array, regex_arrays)

    onboarding_file_generation(app_name, 'MPDS', 'Data Contract', mpds_data_contract_content, '.yaml', '')
    onboarding_file_generation(app_name, 'MPDS', 'Query Template', mpds_query_template_content, '.yaml', '')