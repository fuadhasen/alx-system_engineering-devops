#!/usr/bin/python3
""" python script Export to json
"""
import csv
import json
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

    list_task = []
    for task in tasks:
        list_task.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user.get('username')
        })

    data = {user.get('id'): list_task}

    filename = '{}.json'.format(user.get('id'))
    with open(filename, 'w', encoding='utf-8') as _file:
        json.dump(data, _file, indent=4)
