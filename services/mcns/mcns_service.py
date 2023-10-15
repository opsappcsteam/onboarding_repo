import uuid
import json
from collections import Counter

def uuid_generator(template_id_array):
    uuid_template_id_array = []
    for template_id in template_id_array:
        if template_id == 'nan' or template_id == '<Will be given by AppCS Onboarding Team>' or template_id == '<This will be filled up by AppCS Onboarding Team>':
            template_id = '<channel_type>' + str(uuid.uuid4()).replace('-', '')
            uuid_template_id_array.append(template_id)
        else:
            uuid_template_id_array.append(template_id)
    return uuid_template_id_array

def channel_type_converter(channel_type_array):
    converted_channel_type_array = []
    for channel_type in channel_type_array:
        channel_type = channel_type.lower()
        converted_channel_type_array.append(channel_type)
    return converted_channel_type_array

def template_id_converter(template_id_array, channel_type_array):
    converted_template_id_array = []
    i = 0
    while i < len(template_id_array):
        if '<channel_type>' in template_id_array[i]:
            template_id = template_id_array[i].replace('<channel_type>', channel_type_array[i])
            converted_template_id_array.append(template_id)
        else:
            converted_template_id_array.append(template_id_array[i])
        i += 1
    return converted_template_id_array

def regex_json_converter(regex_json_array):
    converted_regex_json_array = []
    for json_item in regex_json_array:
        item = json_item.split("\n")
        item = ' '.join(line.lstrip() for line in item)
        regex_json = item.replace('\\', '\\\\\\\\').replace('"', '\\"')
        converted_regex_json_array.append(regex_json)
    return converted_regex_json_array

def regex_validator(regex_json_array):
    validated_regex_json_array = []
    for regex_json in regex_json_array:
        try:
            regex_json.loads(value)
            validated_regex_json_array.append(True)
        except (json.JSONDecodeError, TypeError):
            validated_regex_json_array.append(False)

def invalid_regex_identifier(array):
    false_array = []
    i = 0
    while i < len(array):
        if array[i] == False:
            false_array.append(i)
        i += 1
    return false_array

def most_common_length_getter(array):
    counts = Counter(array)
    most_common = counts.most_common(1)
    most_common_element, most_common_count = most_common[0]
    return most_common_length
        
