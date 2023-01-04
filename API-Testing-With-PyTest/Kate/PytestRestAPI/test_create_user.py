import json
import requests
from decouple import config

url = config('DOMAIN') + "/students"

def test_create_new_user():
        file_data = open('./RestAPI/post_data.json', 'r')

        json_input = file_data.read()
        request_json = json.loads(json_input)

        response = requests.post(url, request_json)
        assert response.status_code == 201

def test_get_user_data():
        response = requests.get(url)
        print(response.text)
        assert response.status_code == 200
