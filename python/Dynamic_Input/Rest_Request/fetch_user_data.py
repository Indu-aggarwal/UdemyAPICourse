import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)

#print(response)

# validate status code
assert response.status_code == 200

print(response.headers.get('Date'))
print(response.headers.get('Server'))

print(response.cookies)

print(response.encoding)

print(response.content)

json_response = json.loads(response.text)

pages = jsonpath.jsonpath(json_response,'total_pages')
print(pages[0])

assert pages[0] == 2

email_data = jsonpath.jsonpath(json_response,'data')
for i in range( len( response.json()['data'] )):
        print(jsonpath.jsonpath(json_response,'data['+str(i)+'].email'))
