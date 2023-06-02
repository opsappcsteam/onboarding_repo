import sys
from Services.shared_functions import get_excel_name
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
    print('''🚫 ERROR 🚫
No Excel Detected
''')
    sys.exit()

print(f'Excel Detected: {get_excel_name()}')
env = input('What environment are you onboarding to? (sit/prod): ').lower()

if env not in env_array:
    print('''
🚫 ERROR 🚫
The environment you selected is incorrect; Run the program again!
''')
    sys.exit()

try:
    version = input('Which onboarding version are you using? (1 / 2): ')
    if version not in version_array:
        print('''
🚫 ERROR 🚫
The version you selected is invalid; Run the program again!
''')
        sys.exit()

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
    print('''
🚫 ERROR 🚫
The version you selected is incorrect; Run the program again!
''')
