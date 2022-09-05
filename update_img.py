import json, glob
from collections import OrderedDict
from pprint import pprint as pp

# constant
START_ID = 0
MAX_ID = 999
DATA_DIR = 'data'
IMG_URL = "https://jigsaw.diew.app/pass_img/?tier={}&score={}"

# action config
WRITE_FILE = False
FROM_ID = START_ID
TO_ID = MAX_ID

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

    # get current tier
    tier_idx = find_index(attrs, 'trait_type', 'Tier')
    if tier_idx == -1:
        print(path)
        pp(data)
        raise Exception("ERROR: tier not found")
    tier_info = attrs[tier_idx]
    tier = tier_info['value'].lower()
 
    # update img
    data['image'] = IMG_URL.format(tier, point)

    print("ID#{} tier: {}, point: {}".format(token_id, tier, point))

    if WRITE_FILE:
        with open(path, "w") as f:
            json.dump(data, f)
    else:
        print("--> {}".format(path))
        pp(data)
