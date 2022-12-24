#!/usr/bin/python3
"""
This script takes 2 args in order to
solve backend position challenge
1st arg is repository name
2nd arg is owner name
use requests and sys packages
"""


import sys
import requests
if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            sys.argv[2], sys.argv[1])
    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
