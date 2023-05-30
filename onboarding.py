from Services.shared_functions import get_excel_name
from Services.MCNS.mcns import mcns_onboarding
from Services.MDS.mds import mds_onboarding
from Services.SFT.sft import sft_onboarding

excel_name = get_excel_name()
if excel_name != None:
    print(f'Excel Detected: {get_excel_name()}')
    env_array = ['sit', 'prod']
    version_array = ['1', '2']
    env = input('What environment are you onboarding to? (sit/prod): ').lower()
    if env in env_array:
        try:
            version = input('Which onboarding version are you using? (1 / 2): ')
            if version in version_array:
                mds_onboarding(version)
                mcns_onboarding(env)
                sft_onboarding(env)
            else:
                print('The version you selected is invalid; Run the program again!')
        except ValueError:
            print('The version you selected is incorrect; Run the program again!')
    else:
        print('The environment you selected is incorrect; Run the program again!')
else:
    print('No Excel Detected')
