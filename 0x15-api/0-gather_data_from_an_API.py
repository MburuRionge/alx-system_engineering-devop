#!/usr/bin/python3
'''
gathers information about an employee by ID and returns their TODO progress
'''
import requests
import sys


def info():
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    emp_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{emp_id}')
    if emp_response.status_code != 200:
        print(f"Error: Failed to retrieve employee information. Status code: {emp_response.status_code}")
        sys.exit(1)

    employee_data = emp_response.json()
    name = employee_data.get('name')
    
    tasks_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    if tasks_response.status_code != 200:
        print(f"Error: Failed to retrieve task information. Status code: {tasks_response.status_code}")
        sys.exit(1)

    tasks_data = tasks_response.json()
    complete = 0
    titles = []
    total = 0
    for task in tasks_data:
        if task['userId'] == emp_id:
            if task['completed']:
                complete += 1
                titles.append(task['title'])
            total += 1

    print(f"Employee {name} is done with tasks ({complete}/{total}):")
    for title in titles:
        print('\t', title)


if __name__ == "__main__":
    info()
