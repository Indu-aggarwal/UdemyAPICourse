import pytest


@pytest.mark.Smoke
@pytest.mark.Sanity
def test_printing():
    print("Smoke test")
    print("This is  a second line of the test")


@pytest.mark.Sanity
@pytest.mark.Regression
def test_of_more_printing():
    print("Sanity and Regression test")
    print("This is  a second line of the test")
