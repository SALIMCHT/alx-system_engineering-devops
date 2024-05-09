#!/usr/bin/python3
"""this is function file"""


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit
    """
    import requests

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    Hdrs = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=Hdrs, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    data = response.json()['data']['children']

    if len(data) == 0:
        print("None")
        return

    for _ in data:
        print(_['data']['title'])
