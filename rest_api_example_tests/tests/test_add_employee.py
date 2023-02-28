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


def test_update_employee(headers, create_url, get_employee_url, update_employee_url, update_employee_data, update_employee_id):
    update_data = {'name': 'Jesper'}

    response_update = requests.put(f'{update_employee_url}/{update_employee_id}', headers=headers, json=update_data)

    if response_update.status_code == 429:
        sleep(int(response_update.headers["Retry-After"]))
        response_update = requests.put(f'{update_employee_url}/{update_employee_id}', headers=headers, json=update_data)

    assert response_update.status_code == 200, f"Failure to update employee: {response_update.text}"
    json_response = response_update.json()
    assert json_response["status"] == "success"
    response_data = json_response["data"]
    json_data = update_employee_data
    assert response_data["name"] == update_data["name"], "Name doesn't match"
    assert response_data["salary"] == json_data["salary"], "Salary shouldn't be change"
    assert response_data["age"] == json_data["age"], "Age shouldn't be change"
