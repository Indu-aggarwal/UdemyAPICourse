import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)

#print(response)

# validate status code
assert response.status_code == 200

print("Headers are: ", response.headers)
print("Header - Date: ",response.headers.get('Date'))
print("Header - Server: ", response.headers.get('Server'))

print("Cookies are: ", response.cookies)

print("Encoding response is: ", response.encoding)

print("Content response is: ", response.content)

json_response = json.loads(response.text)

pages = jsonpath.jsonpath(json_response,'total_pages')
print(pages[0])

assert pages[0] == 2

email_data = jsonpath.jsonpath(json_response,'data')
for i in range( len( response.json()['data'] )):
        print(jsonpath.jsonpath(json_response,'data['+str(i)+'].email'))
