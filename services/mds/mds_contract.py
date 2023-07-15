def mds_contract_entry(table_name, field_array):
    field_array = str(field_array).replace("'", '')

    contract_entry = f'''
-   tablename: {table_name}
    columns: {field_array}
    limit: null
    allow_aggregations: false
'''
    return contract_entry

def mds_contract_content(app_name, pop_svc_array, table_name_array, field_arrays):
    if table_name_array != []:
        pop_array = []
        svc_array = []
        for item in pop_svc_array:
            if item.isdigit():
                item = f'"{item}"'
                svc_array.append(item)
            else:
                pop_array.append(item)

        content = f'''---
role: [{app_name}]
filter: {{
    it0001_persg: {str(pop_array).replace("'", '').replace(' ', '')}, # e.g [A,B,C]
    it0001_werks: {str(svc_array).replace("'", '').replace(' ', '')}  # e.g ["0001","0002","0003"]
}}

table:'''

        table_name_array = list(map(lambda x: x.lower(), table_name_array))

        i = 0
        while i < len(table_name_array):
            field_arrays[i] = list(map(lambda x: x.lower(), field_arrays[i]))
            content += mds_contract_entry(table_name_array[i], field_arrays[i])
            i += 1
        return content
    return None
