import json
import requests
from decouple import config

url = config('DOMAIN') + "/students"

file = open('./post_data.json', 'r')

json_input = file.read()
request_json = json.loads(json_input)

response = requests.post(url, request_json)
# print(response.content)
assert response.status_code == 201
