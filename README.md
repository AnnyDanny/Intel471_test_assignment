# Intel471_test_assignment

## RestApi tests:
### Run without Docker:
#### Prerequisites
Make sure you have installed ___python3___ and ___virtualenv___
#### Preparation for Linux
``cd /rest_api_example_tests``
``virtualenv venv``
``source ./venv/bin/activate``
``pip install -r requirements.txt``
#### How to run tests:
``pytest -v``
### Run with Docker:
#### Prerequisites
Make sure you have installed ___Docker___ and ___Docker Compose___
#### How to run tests:
``docker-compose up``

## UI tests
### Run without Docker:
#### Prerequisites
Make sure you have installed ___npm___ and ___node.js___
#### Preparation
``npm install``
#### How to run tests:
``npx cypress run``
### Run with Docker:
#### Prerequisites
Make sure you have installed ___Docker___ and ___Docker Compose___
``docker-compose up``
