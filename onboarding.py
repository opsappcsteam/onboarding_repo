try:
    from shared_functions import get_excel_name
    print(f'Excel Detected: {get_excel_name()}')
    env = input('What environment are you onboarding to? (sit/prod) : ')
    from mcns import mcns_onboarding
    mcns_onboarding(env)
    import mds
    from sft import sft_onboarding
    sft_onboarding(env)
except ValueError:
    print('No Excel File Found!')
