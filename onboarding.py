from shared_functions import get_excel_name
from mcns import mcns_onboarding
from sft import sft_onboarding

excel_name = get_excel_name()
if excel_name != None:
    print(f'Excel Detected: {get_excel_name()}')
    env = input('What environment are you onboarding to? (sit/prod): ')
    print('Ensure input is in lowercase!')
    mcns_onboarding(env)
    import mds
    sft_onboarding(env)
else:
    print('No Excel Detected')
