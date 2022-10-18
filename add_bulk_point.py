import json, glob, sys
from collections import OrderedDict
from pprint import pprint as pp
from helper import find_index

# log
# 20220905 00:19 [welcome points] add first 100 members (ID 1-100) 100 points
# 20221019 01:03 [celebrate minted out] add 100 points to all members

# constant
START_ID = 0
MAX_ID = 999
DATA_DIR = 'data'

# action config
WRITE_FILE = False
FROM_ID = 1
TO_ID = 999
ADD_POINT = 100

# argv
if (len(sys.argv) > 1):
    if sys.argv[1] == "CONFIRM":
        WRITE_FILE = True

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
