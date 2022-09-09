import json, glob
from collections import OrderedDict
from pprint import pprint as pp

# log
# 20220905 00:19 [welcome points] add first 100 members (ID 1-100) 100 points

# constant
START_ID = 0
MAX_ID = 999
DATA_DIR = 'data'

# action config
WRITE_FILE = False
FROM_ID = 1
TO_ID = 100
ADD_POINT = 100

# helper
def find_index(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1

# main
for token_id in range(FROM_ID, TO_ID+1):
    path = "{}/{}.json".format(DATA_DIR, token_id)

    # load json
    data = json.load(open(path), object_pairs_hook=OrderedDict)
    attrs = data['attributes']

    # get current point
    point_idx = find_index(attrs, 'trait_type', 'Point')
    if point_idx == -1:
        print(path)
        pp(data)
        raise Exception("ERROR: point not found")
    point_info = attrs[point_idx]
    point = int(point_info['value'])

    # update point
    new_point = point + ADD_POINT
    point_info['value'] = str(new_point)

    print("ID#{} add {} points | {} -> {}".format(token_id, ADD_POINT, point, new_point))

    if WRITE_FILE:
        with open(path, "w") as f:
            json.dump(data, f)
    else:
        print("--> {}".format(path))
        pp(data)
