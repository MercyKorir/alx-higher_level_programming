#!/usr/bin/python3
"""Qqueries the reddit api and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    headers = {
        'User-Agent': 'MyBot/1.0'
    }
    response = requests.get("https://www.reddit.com/r/{}/about.json".format(
        subreddit), headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return (0)
