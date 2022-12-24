#!/usr/bin/python3
"""
This script takes in a url, sends
request to url and displays body of
response in utf-8
Requirements:
    manage urllib.error.HTTPError exceptions
    print Error code:
    followed by http status code
use urllib and sys packages
import only urllib and sys
must use with statement
"""


import sys
import urllib.request
if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            body_utf8 = body.decode("utf-8")
            print(body_utf8)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
