FROM python:3.9-slim
COPY . /rest_api_example_tests
WORKDIR /rest_api_example_tests
RUN pip install --no-cache-dir -r requirements.txt
CMD ["pytest", "-v", "--junitxml=reports/result.xml"]
