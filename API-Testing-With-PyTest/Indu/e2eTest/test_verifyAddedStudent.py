import requests
from decouple import config
import json
import pytest
import jsonpath

studentEndpoint = config('DOMAIN') + "/students"
commentsEndpoint = config('DOMAIN') + "/comments"
profileEndpoint = config('DOMAIN') + "/profile"


# @pytest.fixture(scope="module")
# def fixture_code(request_json):
#     studentTestDataFile = open('./studentTestData', 'r')
#     request_json = json.loads(studentTestDataFile.read())

# def test_addNewStudent(fixture_code):
def test_addNewStudent():
    studentInput = open('./studentTestData.json', 'r')
    request_json = json.loads(studentInput.read())
    response = requests.post(studentEndpoint,request_json)
    # print (response.text)
    studentId = jsonpath.jsonpath(response.json(),'id')
    # print(studentId[0])


    commentsInput = open('./commentsTestData.json', 'r')
    request_json = json.loads(commentsInput.read())
    request_json['id'] = int(studentId[0])
    request_json['studentId'] = str(studentId[0])
    response = requests.post(commentsEndpoint,request_json)
    # print(response.text)


    profileInput = open('./profileTestData.json', 'r')
    request_json = json.loads(profileInput.read())
    print(request_json)
    request_json['id'] = int(studentId[0])
    request_json['studentId'] = str(studentId[0])
    response = requests.post(profileEndpoint,request_json)
    print(response.text)
