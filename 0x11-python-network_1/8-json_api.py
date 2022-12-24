#!/usr/bin/python3
"""
This script takes in a letter and sends
post request to url with letter as param
url:
    http://0.0.0.0:5000/search_user
letter to be sent in variable q
if no arg given, set q=""
use requests and sys package
"""


import requests
import sys
if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 1:
        q = ""
        print("No result")
    else:
        q = sys.argv[1]
    params = {"q": q}
    r = requests.post(url, data=params)
    try:
        json_response = r.json()
        if json_response == {}:
            print("No result")
        else:
            id = json_response.get("id")
            name = json_response.get("name")
            print("[{}] {}".format(id, name))
    except (ValueError, TypeError):
        print("Not a valid JSON")
