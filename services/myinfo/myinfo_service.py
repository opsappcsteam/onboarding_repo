def myinfo_array(sheet_info):
    row_array = []
    for index, row in sheet_info.iterrows():
        i = 0
        while i < len(sheet_info.columns):
            if row[i] == True or row[i] == False:
                row_array.append(str(row[i]))
            i += 1
    return row_array

def attributes_converter(attributes_array):
    attributes_map = []
    del attributes_array[:1]
    if len(attributes_array) == 17:
        attributes_map = ['uinfin', 'name', 'sex', 'race', 'dialect', 'dob', 'birthcountry', 'regadd', 'marital', 'email', 'mobileno', 'occupation', 'employment', 'childrenbirthrecords.birthcertno', 'childrenbirthrecords.name', 'childrenbirthrecords.sex', 'childrenbirthrecords.dob']
    elif len(attributes_array) == 18:
        attributes_map = ['uinfin', 'name', 'sex', 'race', 'dialect', 'nationality', 'dob', 'birthcountry', 'regadd', 'marital', 'email', 'mobileno', 'occupation', 'employment', 'childrenbirthrecords.birthcertno', 'childrenbirthrecords.name', 'childrenbirthrecords.sex', 'childrenbirthrecords.dob']
    converted_array = []
    i = 0
    while i < len(attributes_map):
        if attributes_array[i] == 'True':
            converted_array.append(attributes_map[i])
        i += 1
    return converted_array

def redirect_uri_converter(redirect_uri):
    redirect_uri = str(redirect_uri).replace('[', '').replace(']', '').replace("'", '')
    return redirect_uri

def authenticated_flow_converter(authenticated_flow):
    if authenticated_flow == 'yes':
        authenticated_flow = 'true'
    if authenticated_flow == 'no':
        authenticated_flow = 'false'
    return authenticated_flow
