#!/usr/bin/python3
"""Queries employee details

This module is meant to query for an employee's
information and tasks done.

Checks for the completed tasks and prints the completed tasks' titles

Resources:
    * https://jsonplaceholder.typicode.com/

This file contains the following functions:
    * prepare_get_employee_info_url - returns the url for employer info
    * get_employee_info - returns employee information
    * get_employee_todos - returns todos of an employee
    * get_completed_todos - returns completed todos
"""

import json
from requests import Request, Session, exceptions, get
import sys


def prepare_get_employee_info_url(employee_id):
    """Prepares the employee info url

    Args:
        employee_id (str): The id of employee

    Returns:
        (str): The url
    """

    if employee_id is None:
        return None
    return f"https://jsonplaceholder.typicode.com/users/{employee_id}"


def get_employee_info(employee_id):
    """Gets employee information

    Args:
        employee_id (str): The ID of the employee

    Returns:
        (dict): The employee details
    """

    request = Request(
        method="get",
        url=prepare_get_employee_info_url(employee_id)
    )
    session = Session()
    prepared_request = session.prepare_request(request)

    try:
        response = session.send(prepared_request)
        response.raise_for_status()
        return response.json()
    except exceptions.HTTPError as e:
        print(f"Request failed with status code", e.response.status_code)
        return None


def get_employee_todos(employee_id):
    """Make request to the API

    Args:
        employeeId (str): The ID of the employee

    Returns:
        API response
    """

    url = f"https://jsonplaceholder.typicode.com/todos"

    request = Request(method="get", url=url, params={"userId": employee_id})
    session = Session()
    prepared_request = session.prepare_request(request=request)

    try:
        response = session.send(prepared_request)
        response.raise_for_status()
        return response.json()
    except exceptions.HTTPError as e:
        print(f"Failed with status code: {e.response.status_code}")
        return None


def get_all_employees():
    """Gets all employees

    Queries for all employees
    """

    url = "https://jsonplaceholder.typicode.com/users"
    response = get(url).json()
    if response is None:
        return None
    return response


def get_completed_todos(todos=[]):
    """Gets completed todos

    Args:
        todos (list): Todos to check

    Returns:
        (list): completed todos
    """

    return [todo for todo in todos if todo.get('completed')]


def export_to_json(filename, data):
    """Exports Todos to JSON

    Creates a JSON file containing the Todos

    Args:
        filename (str): Name of file
        data (dict): The data to export
    """

    with open(f'{filename}.json', mode='w') as file:
        json.dump(data, file)


def format_todos(todos=[], employee_info={}):
    """Format todos to desired format"""
    return [{
        "username": employee_info.get("username"),
        "task": todo.get("title"),
        "completed": todo.get("completed")
    } for todo in todos]


if __name__ == '__main__':

    employees = get_all_employees()
    if (employees is None):
        exit(1)

    data = {}
    for employee in employees:
        employee_id = employee.get("id")
        if (employee_id is None):
            continue

        employee_info = get_employee_info(employee_id)
        employee_todos = get_employee_todos(employee_id)
        data[employee_id] = format_todos(employee_todos, employee_info)
    export_to_json('todo_all_employees', data)
