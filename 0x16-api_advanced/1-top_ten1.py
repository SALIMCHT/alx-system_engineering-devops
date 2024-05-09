#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """Tasks Reddit user name and returns the subscribers number."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        if data:
            for post in data:
                print(post['data']['title'])
        else:
            print("No posts found for the given subreddit.")
    else:
        print("None")


if __name__ == '__main__':
    from sys import argv
    top_ten(argv[1] if len(argv) > 1 else '')
