# -v (verbose) to print all the tests and their pass/fail status
# ********************************************************************************
# -s to print the output on the console
# ********************************************************************************
# -k to run the specific test (-k <name_of_the_test> <folder_name_option>)
# -k to run the specific tests that contains the same test string (pytest -v -s -k test_002)
# ********************************************************************************
# -m to run the specific tagged test (pytest -v -s -m Regression)
# -m also used to skip the specific tagged tests (pytest -v -s -m "not Regression")

import pytest

# Decorator (@here "Regression" is user defined name)

@pytest.mark.Regression
def test_001_tag():
    print("This is my first test case")

@pytest.mark.Smoke
def test_002_tag():
    print("student list is: ")