#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id
"""
import urllib.request
import sys


if __name__ == "__main__":
    """
    func definition
    """
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.info()["X-Request-Id"])
