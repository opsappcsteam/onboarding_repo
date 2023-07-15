def row_array(sheet_info, anchor_value, step):
    row_array = []
    for index, row in sheet_info.iterrows():
        i = 0
        while i < len(sheet_info.columns):
            if row[i] == anchor_value:
                row_array.append(str(row[i + step]))
            i += 1
    return row_array

def column_array(sheet_info, header):
    column_array = []
    column = []
    start_index = []
    end_index = []
    for index, row in sheet_info.iterrows():
        i = 0
        while i < len(sheet_info.columns):
            if row[i] == header:
                start_index.append(index + 1)
                column.append(i)
            if row[i] == '<Add more entries here if necessary>' or row[i] == 'Whitelisting Query Template (Stage 2)':
                end_index.append(index)
            i += 1
    if start_index != []:
        for item in sheet_info.iloc[start_index[0]:end_index[0], column[0]]:
            column_array.append(str(item))
    return column_array
