import json
import requests
from decouple import config

studentId = "/2"
url = config('DOMAIN') + "/students" + studentId

file = open('./patch_data.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

response = requests.patch(url, request_json)
assert response.status_code == 200

# load the last name updated student data
json_response = json.loads(response.text)
updated_middle_name = json_response["middleName"]
updated_last_name = json_response["lastName"]
print(updated_middle_name, "\n", updated_last_name)
