import requests

url = "https://reqres.in/api/users/2"

deleted_response = requests.delete(url)
print(deleted_response.status_code)

assert deleted_response.status_code == 204
