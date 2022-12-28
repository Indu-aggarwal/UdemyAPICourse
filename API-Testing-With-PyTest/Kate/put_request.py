import json
import jsonpath
import requests
from decouple import config

updated_studentId = "/2"
url = config('DOMAIN') + "/students" + updated_studentId
file = open('./put_data.json', 'r')

json_input = file.read()
request_json = json.loads(json_input)

response = requests.put(url, request_json)
assert response.status_code == 200

# load the updated student data
json_response = json.loads(response.text)
# extract specific student data into to retrieve it with jsonpath
first_name = jsonpath.jsonpath(json_response, "firstName")
print(first_name[0])

# we can achieve the above differently without using jsonpath
json_res = json.loads(response.content)
last_name = json_res["lastName"]
print(last_name)

