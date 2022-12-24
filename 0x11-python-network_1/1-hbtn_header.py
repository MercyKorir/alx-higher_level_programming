#!/usr/bin/python3
"""
This script takes in a URL, sends request to it
and displays the value of the X-Request-Id variable
found in the header of the response
using urllib and sys packages
must use with statement
"""


import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        id = dict(response.headers).get("X-Request-Id")
        print(id)
