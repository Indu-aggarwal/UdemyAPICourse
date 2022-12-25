import pytest

# Test cases should be written inside a methods
# PyTest function should start with test key words
num = 5


@pytest.mark.skipif(num >= 5, reason='This is the reason the test is skip')
def test_two_another_printing():
    print("Test on second test in PyTest")
    print("This is  a second line of the test")


@pytest.mark.Sanity
@pytest.mark.Smoke
def test_third_another_printing():
    print("Test on third test in PyTest")
    print("This is  a second line of the test")
