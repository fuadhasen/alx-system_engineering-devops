#!/usr/bin/python3
"""
script fetch Reddit API and returns top 10 hot post
"""

import requests


def top_ten(subreddit):
    """function for api request"""
    url = "https://api.reddit.com/r/{}/hot?limit=10".format(
            subreddit)
    headers = {'User-Agent': 'CustomClient/1.0'}

    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        print('None')
        exit()

    res = res.json()
    data = res.get('data', {}).get('children', [])
    print([d['data']['title'] for d in data])
