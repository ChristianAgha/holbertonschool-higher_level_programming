#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    """
    Fetches https://intranet.hbtn.io/status
    """
    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
