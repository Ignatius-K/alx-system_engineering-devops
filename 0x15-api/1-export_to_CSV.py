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

import csv
from requests import Request, Session, exceptions, request
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


def get_completed_todos(todos=[]):
    """Gets completed todos

    Args:
        todos (list): Todos to check

    Returns:
        (list): completed todos
    """

    return [todo for todo in todos if todo.get('completed')]


def export_to_csv(employee_id, todos=[], field_names=[]):
    """Exports Todos to CSV

    Creates a CSV file containing the Todos

    Args:
        employee_id (str): The Id of the employee
        todos (list): Th todos to export_to_csv
    """

    with open(f'{employee_id}.csv', mode='w') as file:
        file_writer = csv.DictWriter(
            file,
            field_names,
            quoting=csv.QUOTE_ALL,
            extrasaction='ignore'
        )
        for todo in todos:
            file_writer.writerow(todo)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} {{employee_id}}')
        exit()

    employee_id = sys.argv[1]

    employee_info = get_employee_info(employee_id)

    employee_todos = get_employee_todos(employee_id)
    if (employee_info is None or
            employee_todos is None or
            type(employee_todos) is not list):
        exit(1)

    formatted_todos = [
        {
            **todo,
            "name": employee_info.get("username")
        } for todo in employee_todos
    ]
    export_to_csv(
        employee_id,
        formatted_todos,
        field_names=['userId', 'name', 'completed', 'title']
    )
