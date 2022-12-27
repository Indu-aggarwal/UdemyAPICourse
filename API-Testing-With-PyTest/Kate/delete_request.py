import requests
import json
from decouple import config

base_url = config('DOMAIN') + "/students"

response = requests.get(base_url)
json_response = json.loads(response.content)

response_array = []
for i in json_response:
        response_array.append(i["id"])

if len(response_array) != 0:
        last_element = response_array[- 1]
        endpoint = base_url + "/" + str(last_element)
        response = requests.delete(endpoint)
        assert response.status_code == 200
else:
        print("Nothing to delete.")

