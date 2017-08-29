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
    r = requests.get(u).json()
    if type(r) is dict:
        if r.get("message") == "Not Found":
            r = None
    com_lst = []
    if (r):
        for item in r:
            sha = item["sha"]
            name = item["commit"]["author"]["name"]
            com_lst.append([sha, name])
        if len(com_lst) >= 10:
            for n in range(10):
                print("{}: {}".format(com_lst[n][0], com_lst[n][1]))
        else:
            for n in range(len(com_lst)):
                print("{}: {}".format(com_lst[n][0], com_lst[n][1]))
