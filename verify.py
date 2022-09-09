#!/usr/bin/python

import sys
import json
from collections import OrderedDict
from datetime import datetime
from pprint import pprint as pp
from helper import *

DATA_DIR = 'data'

# load json data
token_id = sys.argv[1]
path = "{}/{}.json".format(DATA_DIR, token_id)
data = json.load(open(path), object_pairs_hook=OrderedDict)

# verified ?
(idx, verified_date) = get_safe_trait_value(data, "Verified")

# exit if verified
if idx != -1:
    print("already verified at {}".format(verified_date))
    exit()

# stamp verified date
stamp = datetime.now().strftime('%Y/%m/%d')
data['attributes'] += [OrderedDict({
    'trait_type': 'Verified',
    'value': stamp,
})]

# save
pp(data)
write_file(path, data)
