import json
import requests

url = "https://reqres.in/api/users/2"

json_file = open("./input_json.json",'r')

json_input = json_file.read()
request_json = json.loads(json_input)

response_file = requests.post(url, request_json)
print(response_file.content)

assert response_file.status_code == 201

print(response_file.headers.get('Content-Type'))

response_text = json.loads(response_file.text)
print(response_text)
