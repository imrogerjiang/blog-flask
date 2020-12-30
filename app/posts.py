import json
import os
from datetime import date
from flask import Markup

# Load all json from content/posts into list
all_posts = []

for filename in os.listdir("app/static/assets/posts/"):
    if filename.find(".json") > -1:
        with open("app/static/assets/posts/" + filename) as f:
            all_posts.append(json.load(f))

# Post processing
for post in all_posts:
    post["date"] = date.fromisoformat(post["date"])
    post["body"] = Markup(post["body"])

# Returns n most recent posts
def load_recent(n=10, start=0):
    if start > len(all_posts):
        raise ValueError("Start argument larger than number of posts.")
    
    start = min(len(all_posts), start)
    n = min(len(all_posts)-start, n)
    all_posts.sort(key=lambda x:x["date"], reverse=True)
    return all_posts[start:start+n]



if __name__ == "__main__":
    from pprint import pprint

    pprint(load_recent(10))


