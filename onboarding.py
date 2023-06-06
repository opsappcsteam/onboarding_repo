import pandas as pd
from Services.shared_functions import onboarding_error, get_excel_name, get_excel_path
from Services.MCNS.mcns import mcns_onboarding
from Services.MDS.mds import mds_onboarding
from Services.SFT.sft import sft_onboarding

print('''
############################
 AppCS Onboarding Programme
############################
''')    

env_array = ['sit', 'prod']
version_array = ['1', '2']
excel_name = get_excel_name()

if excel_name == None:
    onboarding_error('No Excel')

print(f'Excel Detected: {get_excel_name()}')
env = input('What environment are you onboarding to? (sit/prod): ').lower().strip()

if env not in env_array:
    onboarding_error('Invalid Env')

try:
    version = input('Which onboarding version are you using? (1 / 2): ').strip()
    if version not in version_array:
        onboarding_error('Invalid Version')

    if version == '1':
        pd.read_excel(get_excel_path(), 'MDS')
    elif version == '2':
        pd.read_excel(get_excel_path(), 'MPDS')

    print(f'''
############################
Onboarding Environment: {env.upper()}
Form Version: {version}
############################
    ''')    
    mds_onboarding(version)
    mcns_onboarding(env)
    sft_onboarding(env)
    print()
except ValueError:
    onboarding_error('Incorrect Version')
