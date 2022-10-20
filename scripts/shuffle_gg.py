import random, time
from datetime import datetime
from pprint import pprint as pp

TITLE = "5x WL of Ape Gang GG"
DESC = "Follow @APEGANGGGNFT event"

PRICE_NUM = 5
ROUND_DELAY = 0 #s
DATA_PATH = 'gg_followers.dat'
LOG_PATT = "Round {:03} => {}"

# init data
bulk = [ l.strip() for l in open(DATA_PATH, 'r').readlines() if l.startswith('@') ]
supply = len(bulk)

# basic info
print(TITLE)
print(DESC)
print("")
print("Raffle Time: {}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
print("Members: {}".format(supply))
print("")

# loop
for no in range(supply - PRICE_NUM+1):
    print(LOG_PATT.format(no, bulk))
    if (len(bulk) == PRICE_NUM):
        print("")
        print("Winner is {} 🎉".format(bulk))
    else:
        bulk = bulk[1:]
        random.shuffle(bulk)
        time.sleep(ROUND_DELAY)
