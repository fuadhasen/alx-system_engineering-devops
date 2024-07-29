#!/usr/bin/python3
""" python script Export to CSV
"""
import csv
import requests
import sys


if __name__ == "__main__":
    _id = sys.argv[1]

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

    with open(
        '{}.csv'.format(user.get('id')),
        'w',
        newline=''
    ) as _file:
        writer = csv.writer(_file, quotechar='"', quoting=csv.QUOTE_ALL)
        # format is in this way
        # writer.writerow(["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"])
        for task in tasks:
            writer.writerow([
                task.get('userId'),
                user.get('name'),
                task.get('completed'),
                task.get('title')
            ])
