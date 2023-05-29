from Services.shared_functions import get_excel_name
from Services.MCNS.mcns import mcns_onboarding
from Services.MDS.mds import mds_onboarding
from Services.SFT.sft import sft_onboarding

excel_name = get_excel_name()
if excel_name != None:
    print(f'Excel Detected: {get_excel_name()}')
    try:
        env = input('What environment are you onboarding to? (sit/prod): ').lower()
        mcns_onboarding(env)
        mds_onboarding()
        sft_onboarding(env)
    except IndexError:
        print('Enter a valid environment name; Run the program again!')
else:
    print('No Excel Detected')
