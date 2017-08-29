#!/usr/bin/python3
"""
Takes in a letter and sends a POST request with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    """
    func def
    """
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    if req.json() == {}:
        print("No result")
    else:
        try:
            print("[{}] {}".format(req.json()["id"], req.json()["name"]))
        except:
            print("Not a valid JSON")
