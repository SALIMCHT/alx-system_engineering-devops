#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """ tasks reddit user name and return the subscribers number """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    Hdrs = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=Hdrs,  allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
