import random
from datetime import datetime

TITLE = "Jigsaw Pass Raffle #1 Test Drive"
DESC = "1x Movie Ticket from MajorVerse"

FROM_ID = 1
TO_ID = 262
SKIP_IDS = [ 179 ]

URL = "https://qx.app/asset/0x49Bb981c8b721B9873093f519337329f794E8577/{}"
LOG_PATT = "Round {:03} => {}"

# init data
bulk = [ id for id in range(FROM_ID, TO_ID+1) ]
bulk = list(set(bulk) - set(SKIP_IDS))
supply = len(bulk)

# basic info
print(TITLE)
print(DESC)
print("")
print("Raffle Time: {}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
print("Supply: {} ({}-{})".format(supply, FROM_ID, TO_ID))
print("Skip IDs: {}".format(SKIP_IDS))
print("")

# loop
for no in range(supply):
    print(LOG_PATT.format(no, bulk))
    if (len(bulk) == 1):
        winner_id = bulk[0]
        print("")
        print("Winner is {} 🎉".format(winner_id))
        print(URL.format(winner_id))
    else:
        bulk = bulk[1:]
        random.shuffle(bulk)
