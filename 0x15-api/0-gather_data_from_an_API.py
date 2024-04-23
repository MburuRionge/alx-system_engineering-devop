#!/usr/bin/python3
"""
using this REST API, for a given employee ID, returns information about his/her TODO list progress.
"""
import requests
import sys


def info():
    emp = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    name = requests.get('name')
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = tasks.json()
    complete = 0
    titles = []
    total = 0
    for task in tasks:
        if task['userId'] == int(sys.argv[1]):
            if task['completed'] is True:
                complete += 1
                titles.append(task['title'])
            total += 1
    print("Employee {} is done with tasks({}/{}):".format(name, complete, total))
    for title in titles:
        print('\t ', end="")
        print(title)


if __name__ == "__main__":
    info()