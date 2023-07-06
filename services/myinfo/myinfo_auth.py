def myinfo_authorizer_content(app_name, attributes_array, redirect_uri, authenticated_flow):
    content = f'''[
    {{
        "pk": "{app_name}",
        "attributes": ['''
    for item in attributes_array:
            attribute_entry = f'''
            "{item}",'''
            content += attribute_entry
    content = content[:-1]
    content_footer = f'''
        ],
        "redirect_uri": "{redirect_uri}",
        "authenticated_flow": {authenticated_flow}
    }}
]'''
    content += content_footer

    if content == f'''[
    {{
        "pk": "{app_name}",
        "attributes": [
        ],
        "redirect_uri": "{redirect_uri}",
        "authenticated_flow": {authenticated_flow}
    }}
]''' or redirect_uri == "nan":
        return None
    return content
