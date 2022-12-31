# *** to create fixture ****
# 1. write fixture fixture_code
# 2. define function as fixture function
# 3. provide fixture_code argument in each test

import pytest

# scope module will run the fixture code once in this file
@pytest.fixture(scope="module")
def fixture_code():
    print("This is starting my test case run")
    # Yield is to run the code after the test case run
    yield
    print("This is end of my test case run")

# Decorator (@here "Regression" is user defined name OR customised markers)

@pytest.mark.Regression
@pytest.mark.Smoke
def test_001_fixture(fixture_code):
    print("This is my first test case")

@pytest.mark.Regression
def test_002_fixture(fixture_code):
    print("student list is: ")