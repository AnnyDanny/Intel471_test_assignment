from time import sleep

import pytest
import requests


@pytest.fixture
def headers():
    return {
        'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'),
        'Content-type': 'application/json',
    }


@pytest.fixture
def base_url():
    return 'https://dummy.restapiexample.com/api/v1'


@pytest.fixture
def create_url(base_url):
    return f'{base_url}/create'


@pytest.fixture
def get_employee_url(base_url):
    return f'{base_url}/employee'


@pytest.fixture
def update_employee_url(base_url):
    return f'{base_url}/update'


@pytest.fixture
def update_employee_data():
    json_data = {
        'name': 'Peter',
        'salary': '1234',
        'age': '25',
    }
    return json_data


@pytest.fixture
def update_employee_id(update_employee_data, create_url):
    json_data = update_employee_data
    response = requests.post(create_url, headers=headers, json=json_data)

    if response.status_code == 429:
        sleep(int(response.headers["Retry-After"]))
        response = requests.post(create_url, headers=headers, json=json_data)

    assert response.status_code == 200, f"Failure to create employee: {response.text}"
    json_response = response.json()
    assert json_response["status"] == "success"
    response_data = json_response["data"]
    assert response_data["name"] == json_data["name"], "Name doesn't match"
    assert response_data["salary"] == json_data["salary"], "Salary doesn't match"
    assert response_data["age"] == json_data["age"], "Age doesn't match"

    return response_data["id"]
