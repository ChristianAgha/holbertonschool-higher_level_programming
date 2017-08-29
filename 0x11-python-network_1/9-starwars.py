#!/usr/bin/python3
"""
Takes in a string and sends a search request to the Star Wars API
"""
import requests
import sys


if __name__ == "__main__":
    """
    func def
    """
    req = requests.get("https://swapi.co/api/people/?search=" + sys.argv[1])
    res = req.json()
    print("Number of result: {}".format(res["count"]))
    for item in res["results"]:
        print(item["name"])
