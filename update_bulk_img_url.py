import json, glob, sys
from collections import OrderedDict
from pprint import pprint as pp
from helper import find_index

# constant
START_ID = 0
MAX_ID = 999
DATA_DIR = 'data'
IMG_URL = "https://jigsaw.diew.app/pass_img/?id={}&tier={}&score={}"

# action config
WRITE_FILE = False
FROM_ID = START_ID
TO_ID = MAX_ID

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

    # get current tier
    tier_idx = find_index(attrs, 'trait_type', 'Tier')
    if tier_idx == -1:
        print(path)
        pp(data)
        raise Exception("ERROR: tier not found")
    tier_info = attrs[tier_idx]
    tier = tier_info['value'].lower()
 
    # verified flag
    verified_flag = find_index(attrs, 'trait_type', 'Verified') > -1

    # update img
    data['image'] = IMG_URL.format(token_id, tier, point)
    if verified_flag: data['image'] += '&v=1'

    print("ID#{} tier: {}, point: {}, verified: {}".format(token_id, tier, point, verified_flag))

    if WRITE_FILE:
        with open(path, "w") as f:
            json.dump(data, f)
    else:
        print("--> {}".format(path))
        pp(data)
