from Services.shared_functions import get_excel_name
from Services.MCNS.mcns import mcns_onboarding
from Services.MDS.mds import mds_onboarding
from Services.SFT.sft import sft_onboarding

excel_name = get_excel_name()
if excel_name != None:
    print(f'Excel Detected: {get_excel_name()}')
    try:
        env = input('What environment are you onboarding to? (sit/prod): ').lower()
        version = input('Which onboarding version are you using? (1 / 2): ')
        mds_onboarding(version)
        mcns_onboarding(env)
        sft_onboarding(env)
    except IndexError:
        print('Enter a valid environment name; Run the program again!')
else:
    print('No Excel Detected')
