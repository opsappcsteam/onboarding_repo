def onboard_csv_content(operation_array, project_name, role_array, email_array):
    if 'Onboard' in operation_array:
        onboard_content = 'operation, username, projectName, role, email'
        i = 0
        while i < len(operation_array):
            if operation_array[i] == 'Onboard':
                onboard_content += f'''
ONBOARD, {email_array[i]}, {project_name}, Survey {role_array[i]}, {email_array[i]}'''
            i += 1
        return onboard_content
    return None

def reset_csv_content(operation_array, project_name, role_array, email_array):
    if 'Reset' in operation_array:
        reset_content = 'operation, username, projectName, role, email'
        i = 0
        while i < len(operation_array):
            if operation_array[i] == 'Reset':
                reset_content += f'''
RESET, {email_array[i]}, , , '''
            i += 1
        return reset_content
    return None

def unlock_csv_content(operation_array, project_name, role_array, email_array):
    if 'Unlock' in operation_array:
        unlock_content = 'operation, username, projectName, role, email'
        i = 0
        while i < len(operation_array):
            if operation_array[i] == 'Unlock':
                unlock_content += f'''
UNLOCK, {email_array[i]}, , , '''
            i += 1
        return unlock_content
    return None
