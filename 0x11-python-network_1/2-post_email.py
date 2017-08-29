#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    """
    func definition
    """
    data = {'email': sys.argv[2]}
    data = bytes(urllib.parse.urlencode(data).encode())
    handler = urllib.request.urlopen(sys.argv[1], data)
    print(handler.read().decode('utf-8'))
