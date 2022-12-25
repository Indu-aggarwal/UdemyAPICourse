import json

my_dictionary = '{"value1": "hi","value2": "there"}'

json_respond = json.loads(my_dictionary)

print(json_respond)
