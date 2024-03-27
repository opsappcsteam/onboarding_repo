import json

def myinfo_transformer(myinfo_content, env):
    dynamodb_name = f'myinfo-authorizer-{env}'
    dynamodb_config = {
        dynamodb_name: [
            {
                "PutRequest": {
                    "Item": {

                    }
                }
            }
        ]
    }


    dynamodb_config_items = dynamodb_config.get(f'myinfo-authorizer-{env}')[0].get("PutRequest").get("Item")
    # print(myinfo_content)
    if myinfo_content is None:
        return None

    json_data = json.loads(myinfo_content)
    # print(json_data)
    for key, value in json_data[0].items():
        if key == 'pk' or key == 'redirect_uri':
            dynamodb_config_items[key] = { "S": value }
        elif key == 'authenticated_flow':
            dynamodb_config_items[key] = { "BOOL": value}
        elif key == 'attributes':
            transform_attributes(dynamodb_config_items,value,key)

    return json.dumps(dynamodb_config)

def transform_attributes(dynamodb_config_items, attributes, key):
    attribute_list = []
    attribute_dict = {}
    for attribute in attributes:
        attribute_list.append(
            { "S": attribute }
        )
    
    attribute_dict["L"] = attribute_list
    dynamodb_config_items[key] = attribute_dict


