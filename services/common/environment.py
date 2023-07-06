def get_environment():
    env = ['sit', 'prod']
    user_input = str(input('What environment are you onboarding to? (sit/prod) : ')).lower().strip()
    if user_input in env:
        return user_input
    return None