from time import sleep

import requests


def test_update_employee(headers, create_url, get_employee_url, update_employee_url, update_employee_id):
    update_data = {
        'name': 'Jesper',
        'salary': '321',
        'age': '32',
    }

    response_update = requests.put(f'{update_employee_url}/{update_employee_id}', headers=headers, json=update_data)

    if response_update.status_code == 429:
        sleep(int(response_update.headers["Retry-After"]))
        response_update = requests.put(f'{update_employee_url}/{update_employee_id}', headers=headers, json=update_data)

    assert response_update.status_code == 200, f"Failure to update employee: {response_update.text}"
    json_response = response_update.json()
    assert json_response["status"] == "success"
    response_data = json_response["data"]
    assert response_data["name"] == update_data["name"], "Name doesn't match"
    assert response_data["salary"] == update_data["salary"], "Salary shouldn't be change"
    assert response_data["age"] == update_data["age"], "Age shouldn't be change"
