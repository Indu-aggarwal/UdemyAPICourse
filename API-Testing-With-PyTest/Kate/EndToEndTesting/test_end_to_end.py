import requests
import json
import pytest
from decouple import config
import jsonpath
from faker import Faker

fake = Faker()

url = config('DOMAIN')

@pytest.fixture
def fixture_code(scope="module"):
        global student_data
        student_data = open('./student_data.json', 'r')
        global comments_data
        comments_data = open('./comments_data.json', 'r')
        global profile_data
        profile_data = open('./profile_data.json', 'r')
        yield
        student_data.close()
        comments_data.close()
        profile_data.close()

def test_add_new_student (fixture_code):
        request_json = json.loads(student_data.read())
        request_json['title'] = fake.prefix()
        request_json['firstName'] = fake.unique.first_name()
        request_json['middleName'] = fake.suffix()
        request_json['lastName'] = fake.unique.last_name()
        request_json['dateOfBirth'] = fake.date_of_birth()
        response = requests.post(url + "/students", request_json)
        global student_id
        student_id = jsonpath.jsonpath(response.json(),'id')

        assert response.status_code == 201

def test_add_new_comments(fixture_code):
        requests_json = json.loads(comments_data.read())
        requests_json['id'] = int(student_id[0])
        requests_json['stId'] = student_id[0]
        requests_json['favoriteWords'] = fake.word(), fake.word()
        requests_json['yearExp'] = fake.random_int(0, 20)
        requests_json['lastUsed'] = fake.year()
        response = requests.post(url + "/comments", requests_json)

        assert response.status_code == 201

def test_add_new_profile(fixture_code):
        requests_json = json.loads(profile_data.read())
        requests_json['id'] = int(student_id[0])
        requests_json['stId'] = student_id[0]
        requests_json['email'] = fake.email()
        requests_json['address'] = fake.country(), fake.country_code(), fake.city(), fake.building_number(),fake.postcode(),fake.street_address()
        requests_json['PhoneNumber'] = fake.msisdn()
        requests_json['graduated'] = fake.unique.boolean()
        response = requests.post(url + "/profile", requests_json)

        assert response.status_code == 201
