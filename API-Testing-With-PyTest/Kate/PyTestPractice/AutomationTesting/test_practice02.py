import pytest

@pytest.fixture(scope="module")
def fixture_code():
        print("This is a fixture code which will execute before the testcases are executed")
        print("--------------------------------")
        yield
        print("Close browser after all tests are executed")
        print("--------------------------------")

@pytest.mark.Smoke
def test_registration_simulation(fixture_code):
        print("Testing registration simulation")
        print("Testing two simulation")

num = 5
@pytest.mark.skipif(num > 5, reason="This is the reason for skipping this test")
def test_registration2_simulation(fixture_code):
        print("Testing 02-1 simulation")
        print("Testing 02-2 simulation")
