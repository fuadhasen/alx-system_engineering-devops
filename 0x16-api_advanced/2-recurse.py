#!/usr/bin/python3
"""
script fetch Reddit API and returns title of all hot articles
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """function for api request"""
    url = "https://api.reddit.com/r/{}/hot".format(
            subreddit)
    params = {'after': after}
    headers = {'User-Agent': 'myApp/1.0'}

    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        return None

    res = res.json()
    data = res.get('data', {}).get('children', [])
    for post in data:
        hot_list.append(post['data']['title'])

    # check for pagination
    after = res.get('data', {}).get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
