#!/usr/bin/python3
"""
This script takes url and email,
sends a POST request to url with email as param
and displays the body of response decoded in utf-8
variables:
    email - email given as param
only use urllib and sys packages
only import urllib and sys
must use with
"""


import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    params = {"email": email}
    data = urllib.parse.urlencode(params)
    data = data.encode('ascii')
    with urllib.request.urlopen(urllib.request.Request(url, data)) as response:
        body = response.read()
        body_utf8 = body.decode("utf-8")
        print(body_utf8)
