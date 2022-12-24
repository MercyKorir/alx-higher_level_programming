#!/usr/bin/python3
"""
This script fetches url
url:
    https:alx-intranet.hbtn.io/status
must use requests package
import only requests
"""


import requests
if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    res = r.text
    print("Body response:")
    print("\t- type: {}".format(type(res)))
    print("\t- content: {}".format(res))
