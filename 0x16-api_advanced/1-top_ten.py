#!/usr/bin/python3
"""
script fetch Reddit API and returns top 10 hot post
"""

import requests


def top_ten(subreddit):
    """function for api request"""
    url = "https://api.reddit.com/r/{}/hot".format(
            subreddit)
    headers = {'User-Agent': 'CustomClient/1.0'}

    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        print('None')
        exit()

    res = res.json()
    data = res.get('data', {}).get('children', [])
    if not data:
        print('None')

    for i in range(10):
        title = data[i].get('data').get('title')
        print(title)
