import requests

parameters_set = {
        'MyName': 'Kate',
        'email': 'kate@gmail.com',
        'IdCode': '897654321'
}

response_par = requests.get('https://httpbin.org/get', params=parameters_set)
print(response_par.text)
