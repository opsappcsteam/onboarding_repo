import pandas as pd
from services.common.array_manipulation import *
from services.common.arrays import *
from services.common.file_generation import *
from .mds_contract import *
from .mds_template import *
from .mds_service import *

def mds_main(excel_path, app_name):
    mds_sheet = pd.read_excel(excel_path, 'MDS')
    pop_svc_array = pop_svc_converter(row_array(mds_sheet, True, 1))
    table_name_array = main_name_converter(nan_remover(column_array(mds_sheet, 'Table Name')))
    field_arrays = nan_remover(field_array_splitter(column_array(mds_sheet, 'Table Name'), column_array(mds_sheet, 'Field')))
    mds_data_contract_content = mds_contract_content(app_name, pop_svc_array, table_name_array, field_arrays)

    template_id_array = row_array(mds_sheet, 'Template ID', 3)
    template_array = template_subject_cleaner(row_array(mds_sheet, 'Template', 3), 'MDS')
    regex_arrays = dynamic_values_array_generator([], template_array)
    mds_query_template_content = mds_template_content(app_name, template_array, template_id_array, regex_arrays)

    onboarding_file_generation(app_name, 'MDS', 'Data Contract', mds_data_contract_content, '.yaml', '')
    onboarding_file_generation(app_name, 'MDS', 'Query Template', mds_query_template_content, '.yaml', '')