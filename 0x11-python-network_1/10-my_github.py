#!/usr/bin/python3
"""
Takes Github credentials and uses Github's API to display id
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    func def
    """
    url = "https://api.github.com/users/" + argv[1]
    try:
        r = requests.get(url, auth=(argv[1], argv[2]))
        res = r.json()
        print(res["id"])
    except:
        print("None")
