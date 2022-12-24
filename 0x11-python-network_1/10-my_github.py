#!/usr/bin/python3
"""
This script takes github credentials
uses github api to display your id
"""


import sys
import requests
import requests.auth
if __name__ == "__main__":
    params = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=params)
    id = r.json().get("id")
    print(id)
