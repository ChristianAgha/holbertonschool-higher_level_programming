#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    func def
    """
    u = "https://api.github.com/repos/" + argv[2] + "/" + argv[1] + "/commits"
    try:
        r = requests.get(u)
        res = r.json()
        com_lst = []
        for item in res:
            sha = item["sha"]
            name = item["commit"]["author"]["name"]
            com_lst.append([sha, name])
        for n in range(10):
            print("{}: {}".format(com_lst[n][0], com_lst[n][1]))
    except:
        print("None")
