#!/usr/bin/python

import sys
import json
from collections import OrderedDict
from pprint import pprint as pp
from helper import *

DATA_DIR = 'data'

# load json data
token_id = sys.argv[1]
path = "{}/{}.json".format(DATA_DIR, token_id)
data = json.load(open(path), object_pairs_hook=OrderedDict)

# get point
(idx, point) = get_trait_value(data, "Point")
point = int(point)

# show current point
msg = "current #{} point => {}".format(token_id, point)
print(msg)

# input add point & save
add_point = int(input("add point: "))
data["attributes"][idx]["value"] = str(point + add_point)
pp(data)
write_file(path, data)
