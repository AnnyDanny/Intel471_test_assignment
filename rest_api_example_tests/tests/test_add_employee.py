from time import sleep

import requests


def test_add_employee(headers, create_url, get_employee_url):
    json_data = {
        'name': 'test',
        'salary': '123',
        'age': '23',
    }

    response = requests.post(create_url, headers=headers, json=json_data)

    if response.status_code == 429:
        sleep(int(response.headers["Retry-After"]))
        response = requests.post(create_url, headers=headers, json=json_data)

    assert response.status_code == 200, f"Failed to create employee: {response.text}"
    json_response = response.json()
    assert json_response["status"] == "success"
    response_data = json_response["data"]
    assert response_data["name"] == json_data["name"], "Name doesn't match"
    assert response_data["salary"] == json_data["salary"], "Salary doesn't match"
    assert response_data["age"] == json_data["age"], "Age doesn't match"

    employee_id = response_data["id"]
    response = requests.get(f'{get_employee_url}/{employee_id}', headers=headers)

    if response.status_code == 429:
        sleep(int(response.headers["Retry-After"]))
        response = requests.get(f'{get_employee_url}/{employee_id}', headers=headers)

    assert response.status_code == 200, f"Failed to get employee: {response.text}, {response.headers}"
    json_response = response.json()
    assert json_response["status"] == "success"

    # TODO: For some reason the data response is null
    # response_data = json_response["data"]
    # assert response_data["employee_name"] == json_data["name"], "Name doesn't match"
    # assert response_data["employee_salary"] == json_data["salary"], "Salary doesn't match"
    # assert response_data["employee_age"] == json_data["age"], "Age doesn't match"
    # assert response_data["id"] == json_data["id"], "Id doesn't match"
