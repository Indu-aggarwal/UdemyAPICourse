from urllib import response
import requests

#create a dictionary of headers to send a customized header

headers_data = {
        'value1': 'Header1',
        'value2': 'Header2',
        'value3': 'Header3'
}

url_response = requests.get('https://httpbin.org/get', headers=headers_data)
print(url_response.text)
