#!/usr/bin/python3
"""
This script takes a url, sends request
to url and displays body of response
prints error code
if http status code is greater than or equal to 400
only use requests and sys package
"""


import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    stat_code = r.status_code
    if stat_code >= 400:
        print("Error code: {}".format(stat_code))
    print(r.text)
