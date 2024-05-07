import json

def filter_dict_items (items: list, fields: list):

    filtered_json = {}

    for data in items:
        id = data.key.name
        filtered_json[id] = {
            field: data[field]
            for field in fields
        }

    return json.dumps(filtered_json)