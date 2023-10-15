import sys
import warnings
from services.common.excelsheet import *
from services.common.environment import *
# from services.mcns.mcns_main import mcns_report
# from services.mds.mds_main import mds_report
# from services.mds.mpds_main import mpds_report
# from services.myinfo.myinfo_main import myinfo_report
# from services.sft.sft_main import sft_report
# from services.survey.survey_main import survey_report

warnings.filterwarnings('ignore')
print('''
=========================================================
AppCS Onboarding Report Generator
=========================================================
''')
path = excel_path()
if path is None:
    print('🚫 No Excelsheet Found')
    sys.exit()

env = get_environment()
if env is None:
    print('🚫 Invalid Environment')
    sys.exit()

app_name = excel_name()
sheetlist = excel_sheets()
str_sheetlist = str(sheetlist).replace('[', '').replace(']', '').replace("'", '')
print(f'''
=========================================================
Excelsheet: {app_name}
Services: {str_sheetlist}
Environment: {env.upper()}
=========================================================
''')

# if sheetlist != '🚫 No Services Detected':
#     if 'MCNS' in sheetlist:
#         mcns_report(path, app_name, env)
#     if 'MDS' in sheetlist:
#         mds_report(path, app_name)
#     if 'MPDS' in sheetlist:
#         mpds_report(path, app_name)
#     if 'SFT' in sheetlist:
#         sft_report(path, app_name, env)
#     if 'MyInfo' in sheetlist:
#         myinfo_report(path, app_name)
#     if 'Survey' in sheetlist:
#         survey_report(path, app_name)
#     print('''
=========================================================''')
