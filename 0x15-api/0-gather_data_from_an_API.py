#!/usr/bin/python3
""" python script to Gather data from an API
"""
import requests
import sys


if __name__ == "__main__":
    _id = int(sys.argv[1])

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(_id)
    response = requests.get(url)
    if response.status_code == 200:
        # dict contain user info like name ...
        user = response.json()

    url_2 = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(_id)
    res = requests.get(url_2)
    if res.status_code == 200:
        # list of dict contain user info like tasks ...
        tasks = res.json()

    done_task = 0
    total_task = 0
    titles = []
    for task in tasks:
        if task.get('completed'):
            done_task += 1
            titles.append(task.get('title'))
        total_task += 1

    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), done_task, total_task))
    for title in titles:
        print("\t {}".format(title))
