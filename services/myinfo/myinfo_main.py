import pandas as pd
from services.common.arrays import *
from services.common.file_generation import *
from .myinfo_service import *
from .myinfo_auth import *
from .myinfo_transfomer import *

def myinfo_main(excel_path, app_name, env):
    myinfo_sheet = pd.read_excel(excel_path, 'MyInfo')
    attributes_array = attributes_converter(myinfo_array(myinfo_sheet))
    redirect_uri = redirect_uri_converter(row_array(myinfo_sheet, 'Redirect URL:', 2))
    authenticated_flow = authenticated_flow_converter(myinfo_array(myinfo_sheet)[0].lower())
    myinfo_content = myinfo_authorizer_content(app_name, attributes_array, redirect_uri, authenticated_flow)
    transformed_myinfo_content = myinfo_transformer(myinfo_content,env)
    print(transformed_myinfo_content)
    onboarding_file_generation(app_name, 'MyInfo', 'Authorizer', transformed_myinfo_content, '.json', '')
    # add function here pass env in function