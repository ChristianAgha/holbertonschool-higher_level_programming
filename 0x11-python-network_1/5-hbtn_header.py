#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id
"""
import requests
import sys


if __name__ == "__main__":
    """
    func definition
    """
    if len(sys.argv) > 1:
        req = requests.get(sys.argv[1])
        print(req.headers["X-Request-Id"])
