#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL & displays the body of the response
"""
import urllib.request
import sys


if __name__ == "__main__":
    """
    func definition
    """
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as err:
        print("Error code:", err.code)
