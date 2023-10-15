import sys
import warnings
from services.common.excelsheet import *
from services.common.environment import *
from services.mcns.mcns_main import mcns_onboard
from services.mds.mds_main import mds_onboard
from services.mds.mpds_main import mpds_onboard
from services.myinfo.myinfo_main import myinfo_onboard
from services.sft.sft_main import sft_onboard
from services.survey.survey_main import survey_onboard

warnings.filterwarnings('ignore')
print('''
=========================================================
AppCS Onboarding File Generator
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

if sheetlist != '🚫 No Services Detected':
    if 'MCNS' in sheetlist:
        mcns_onboard(path, app_name, env)
    if 'MDS' in sheetlist:
        mds_onboard(path, app_name)
    if 'MPDS' in sheetlist:
        mpds_onboard(path, app_name)
    if 'SFT' in sheetlist:
        sft_onboard(path, app_name, env)
    if 'MyInfo' in sheetlist:
        myinfo_onboard(path, app_name)
    if 'Survey' in sheetlist:
        survey_onboard(path, app_name)
    print('''
=========================================================''')
