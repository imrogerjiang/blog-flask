import json
import os
from datetime import date
from flask import Markup

class Assets():
    def __init__(self, src=None):
        self.src = src


    # TODO: Implement checking of file address here catch/raise
    def load_asset(self, processing=None):
        self.all_assets = []

        for filename in os.listdir(self.src):
            if filename.find(".json") > -1:
                with open(self.src + filename) as f:
                    self.all_assets.append(json.load(f))

        processing(self.all_assets)

    def load_recent(self, n=10, start=0):
        if self.all_assets is None:
            raise AttributeError("Json assets has not yet been loaded.")

        if start > len(self.all_assets):
            raise ValueError("Start argument larger than number of posts.")
        
        start = min(len(self.all_assets), start)
        n = min(len(self.all_assets)-start, n)
        self.all_assets.sort(key=lambda x:x["date"], reverse=True)
        return self.all_assets[start:start+n]


    
if __name__ == "__main__":
    from pprint import pprint

    def portfolio_processing(portfolio):
        for sample in portfolio:
            sample["date"] = date.fromisoformat(sample["date"])
            sample["body"] = Markup(sample["body"])

    portfolio = Assets(src="app/static/assets/portfolio/")
    portfolio.load_asset(processing=portfolio_processing)
    pprint(portfolio.load_recent(10))





