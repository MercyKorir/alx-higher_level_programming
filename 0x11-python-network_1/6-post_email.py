#!/usr/bin/python3
"""
This script takes url and email,
sends post request to url with email as param
and displays body response
email is variable
"""


import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    params = {"email": email}
    r = requests.post(url, data=params)
    print(r.text)
