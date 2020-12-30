import json
from pprint import pprint

with open("test.json", "r") as f:
    pprint(json.load(f))