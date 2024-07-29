#!/usr/bin/python3
""" python script Export to json , Entire employe data
"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    if response.status_code == 200:
        # list of dict contain user info like name ...
        users = response.json()

    url_2 = 'https://jsonplaceholder.typicode.com/todos'
    res = requests.get(url_2)
    if res.status_code == 200:
        # list of dict contain  all user info like tasks ...
        tasks = res.json()

    data = {}
    for user in users:
        list_task = []
        for task in tasks:
            if task.get('userId') == user.get('id'):
                list_task.append({
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": user.get('username')
                })
                data[user.get('id')] = list_task

    filename = 'todo_all_employees.json.json'
    with open(filename, 'w', encoding='utf-8') as _file:
        json.dump(data, _file)
