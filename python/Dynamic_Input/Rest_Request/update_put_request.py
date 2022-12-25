import json
import requests
import jsonpath

url = "https://reqres.in/api/users/2"


json_file = open("./input_updated_data.json",'r')

json_input = json_file.read()
request_json = json.loads(json_input)

response_file = requests.put(url, request_json)

assert response_file.status_code == 200

updated_response = json.loads(response_file.text)

updated_line = jsonpath.jsonpath(updated_response, 'updatedValue')
