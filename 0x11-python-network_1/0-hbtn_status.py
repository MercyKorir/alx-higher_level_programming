#!/usr/bin/python3
"""
This script fetches a url
    URL: https://alx-intranet.hbtn.io/status
    using urllib
"""


import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
