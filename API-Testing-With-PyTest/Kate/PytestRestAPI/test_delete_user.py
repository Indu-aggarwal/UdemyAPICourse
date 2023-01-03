import requests
import json
from decouple import config
import pytest

base_url = config('DOMAIN') + "/students"

def delete_lastId_student_data(url):
        response = requests.get(url)
        json_response = json.loads(response.content)
        response_array = []
        for i in json_response:
                response_array.append(i["id"])

        if len(response_array) != 0:
                last_element = response_array[- 1]
                endpoint = url + "/" + str(last_element)
                new_response = requests.delete(endpoint)
                assert new_response.status_code == 200
        else:
                print("Nothing to delete.")

def delete_randomId_student_data(url, studentId):
        endpoint = url + "/" + str(studentId)
        updated_response = requests.delete(endpoint)
        assert updated_response.status_code == 200

dataId = 0

@pytest.mark.skip("This test is skipped and can be run when is needed.")
def test_delete_student_data():
        if dataId == 0:
                delete_lastId_student_data(base_url)
        else:
                delete_randomId_student_data(base_url, dataId)

