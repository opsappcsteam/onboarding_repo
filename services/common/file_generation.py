import os

def onboarding_file_generation(app_name, service, file_name, file_content, file_extension, version):
    file_file_name = file_name.lower().replace(' ', '_')
    file_version = '_' + version
    print_version = ' ' + version.capitalize()
    if version == '':
        file_version = ''
        print_version = ''
    if file_content != None:
        with open(f'./artifacts/onboarding/{app_name}-{service}_{file_file_name}{file_version}.txt', 'w', encoding="utf-8") as file:
            file.write(file_content)
        txt_file = os.path.join('./artifacts/onboarding/', f'{app_name}-{service}_{file_file_name}{file_version}.txt')
        output_file = txt_file.replace('.txt', file_extension)
        os.rename(txt_file, output_file)
        print(f'{service} {file_name}{print_version}: Generated')
    else:
        print(f'{service} {file_name}{print_version}: Skipped')

def reporting_file_generation(app_name, report_content):
    with open(f'./artifacts/reports/{app_name}-report.txt', 'w', encoding="utf-8") as file:
        file.write(report_content)
    txt_file = os.path.join('./artifacts/reports/', f'{app_name}-report.txt')
    report_file = txt_file.replace('.txt', '.html')
    os.rename(txt_file, report_file)
    print(f'Report: Generated')
