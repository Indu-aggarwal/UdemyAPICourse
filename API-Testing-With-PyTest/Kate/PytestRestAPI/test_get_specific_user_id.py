import json
import requests
from decouple import config

def test_get_user_data():
        response = requests.get(config('DOMAIN') + "/students/2")
        json_response = json.loads(response.content)
        assert response.status_code == 200
        assert json_response["id"] == 2
