import requests
from decouple import config

response = requests.get(config('DOMAIN') + "/students")

assert response.status_code == 200

