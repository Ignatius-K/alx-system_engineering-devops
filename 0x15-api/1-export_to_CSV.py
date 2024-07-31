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

from requests import Request, Session, exceptions, request
import sys

def prepare_get_employee_info_url(employee_id: str) -> str | None:
    """Prepares the employee info url

    Args:
        employee_id (str): The id of employee

    Returns:
        (str): The url
    """

    if employee_id is None:
        return None
    return f"https://jsonplaceholder.typicode.com/users/{employee_id}"


def get_employee_info(employee_id: str) -> dict | None:
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


def get_completed_todos(todos: list = []):
    """Gets completed todos

    Args:
        todos (list): Todos to check

    Returns:
        (list): completed todos
    """

    return [todo for todo in todos if todo.get('completed')]


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

    employee_completed_todos = get_completed_todos(employee_todos)

    print(f'Employee {employee_info.get("name")} '
          f'is done with tasks({len(employee_completed_todos)}/'
          f'{len(employee_todos)}):')

    for todo in employee_completed_todos:
        print(f'\t {todo.get("title")}')
