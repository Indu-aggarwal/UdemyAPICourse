import pytest


# Test cases should be written inside a methods
# PyTest function should start with test key words

@pytest.mark.Smoke
def test_one_just_printing():
    print("Test on first test in PyTest")
    print("This is  a second line of the test")
