#!/usr/bin/env python3
import requests
from sys import argv


def get_reddit_data(name):
    url = f"https://www.reddit.com/r/{name}/about.json"
    headers = {"User-Agent": "MyRedditBot/1.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()["data"]
        return data
    return "Error"


if __name__ == "__main__":
    if len(argv) < 2:
        print("Please pass an argument for the subreddit to search.")
        exit(1)
    print(get_reddit_data(argv[1]))
