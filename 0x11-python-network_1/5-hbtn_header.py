#!/usr/bin/python3
"""
This script takes url, sends request to it
and displays value of variable X-Request-Id in
response header
use only requests and sys
"""


import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    id = dict(r.headers).get("X-Request-Id")
    print(id)
