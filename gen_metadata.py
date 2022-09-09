import json
 
TOKEN_SIZE = 1000
TOKEN_START = 0
OUTPUT_DIR = 'data'

NAME = "Jigsaw Pass"
DESC = "Welcome to Jigsaw Member System. Enjoy collect points from your activities to earn exclusive rewards."
IMG = "https://diewland.github.io/my-missing-jigsaw-assets/pass/jigsaw_pass_basic.png"

tpl = {
  "name": NAME,
  "description": DESC,
  "image": "<FILL-IN-LOOP>",
  "attributes": [
    {
      "trait_type": "Tier",
      "value": "Basic",
    },
    {
      "trait_type": "Point",
      "value": "0",
    },
  ],
  "compiler": "Jigsaw Engine"
}

for id in range(0, TOKEN_SIZE):
    tpl["name"] = "{} #{}".format(NAME, id)
    tpl["image"] = IMG.format(id)
    with open("{}/{}.json".format(OUTPUT_DIR, TOKEN_START + id), "w") as f:
        json.dump(tpl, f)
