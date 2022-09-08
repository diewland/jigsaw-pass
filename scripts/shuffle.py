import random
from datetime import datetime

TITLE = "Jigsaw Pass Raffle #1 Test Drive"
DESC = "..."

FROM_ID = 1
TO_ID = 262

SUPPLY = TO_ID - FROM_ID + 1
URL = "https://qx.app/asset/0x49Bb981c8b721B9873093f519337329f794E8577/{}"
LOG_PATT = "Round {:03} => {}"

# basic info
print(TITLE)
print(DESC)
print("")
print("Raffle Time: {}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
print("SUPPLY: {} ({}-{})".format(SUPPLY, FROM_ID, TO_ID))
print("")

# init data
bulk = [ id for id in range(FROM_ID, TO_ID+1) ]

# loop
for no in range(SUPPLY):
    print(LOG_PATT.format(no, bulk))
    if (len(bulk) == 1):
        winner_id = bulk[0]
        print("")
        print("Winner is {} 🎉".format(winner_id))
        print(URL.format(winner_id))
    else:
        bulk = bulk[1:]
        random.shuffle(bulk)
