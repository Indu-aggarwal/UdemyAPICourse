import pytest

actual_result = "Testing"

@pytest.mark.Smoke
@pytest.mark.Regression
def test_01_login_logout_simulation():
        print("Testing login simulation")
        print("Testing logout simulation")
        # assert actual_result != "Hello"
        assert actual_result == "Hello"

# decorator for testing
@pytest.mark.skip("This is the reason for the skipping this test")
def test_02_simulation():
        print("Testing 1 simulation")
        print("Testing 2 simulation")
