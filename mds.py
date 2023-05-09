import pandas as pd
import shared_functions as sf
import mds_functions as mf

app_name = sf.get_excel_name()
excelsheet_info = pd.read_excel(sf.get_excel_path(), 'MDS')

template_id_array = mf.mds_array(excelsheet_info, 'Template ID')
template_array = mf.mds_array(excelsheet_info, 'Template')
template_regex_array = mf.mds_array(excelsheet_info, "Template Query Parameter Values' RegEx")

table_name_column_array = mf.column_array(excelsheet_info, 'Table Name')
table_names_array = mf.table_names(table_name_column_array)
field_column_array = mf.column_array(excelsheet_info, 'Field')
field_column_array = list(filter(lambda x: x != 'nan', field_column_array))
field_array_of_arrays = mf.field_array_of_arrays(table_name_column_array, field_column_array)

query_template_content = mf.mds_query_template_yaml(template_array, template_id_array, app_name, template_regex_array)
data_contract_content = mf.data_contract_yaml(app_name, table_names_array, field_array_of_arrays)
query_template_yaml = sf.file_generation(app_name, 'mds_query_template', query_template_content, '.yaml')
data_contract_yaml = sf.file_generation(app_name, 'mds_data_contract', data_contract_content, '.yaml')