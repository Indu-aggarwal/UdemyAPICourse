import requests
from decouple import config

response = requests.get(config('DOMAIN') + "/students")

print(response.text)

assert response.status_code == 200

