import json

def find_index(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1

def get_trait_value(data, key):
    attrs = data["attributes"]
    idx = find_index(attrs, "trait_type", key)
    if idx == -1:
        print(attrs)
        raise Exception("ERROR: {} not found".format(key))
    return (idx, attrs[idx]["value"])

def write_file(path, data):
    with open(path, "w") as f:
        json.dump(data, f)
