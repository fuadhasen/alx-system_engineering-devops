#!/usr/bin/python3
"""
script fetch Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """function for api request"""
    url = "https://api.reddit.com/r/{}/about".format(
            subreddit)
    headers = {'User-Agent': 'CustomClient/1.0'}

    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0

    res = res.json()
    data = res.get('data')
    if data is None:
        return 0

    result = data.get('subscribers')
    return result

