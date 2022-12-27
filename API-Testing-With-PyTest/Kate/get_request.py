import requests

url = "http://localhost:3000/students"

response = requests.get(url)

assert response.status_code == 200

print(response.content)
