#!/usr/bin/python3
"""
This script fetches a url
    URL: https://alx-intranet.hbtn.io/status
    using urllib
"""


import urllib.request
if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        body_size = type(body)
        body_utf8 = body.decode("utf-8")
        print("Body response:")
        print("\t- type: {}".format(body_size))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body_utf8))
