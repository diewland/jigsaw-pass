import random, time
from datetime import datetime
from pprint import pprint as pp

TITLE = "Jigsaw Pass Raffle #1 Test Drive"
DESC = "1x Movie Ticket from MajorVerse"

PRICE_NUM = 2
ROUND_DELAY = 0 #s
DATA_PATH = 'data.dat'
LOG_PATT = "Round {:03} => {}"

# init data
bulk = []
data = [ l.strip() for l in open(DATA_PATH, 'r').readlines() ]
for i in range(0, len(data), 3):
    n = data[i+1]
    s = data[i+2]
    code = "{}**{}".format(n[:3], s[1:])
    bulk.append(code)
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
