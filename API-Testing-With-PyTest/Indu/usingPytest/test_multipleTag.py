# -v (verbose) to print all the tests and their pass/fail status
# ********************************************************************************
# -s to print the output on the console
# ********************************************************************************
# -k to run the specific test (-k <name_of_the_test> <folder_name_option>)
# -k to run the specific tests that contains the same test string (pytest -v -s -k test_002)
# ********************************************************************************
# -m to run the specific tagged test (pytest -v -s -m Regression)
# -m also used to skip the specific tagged tests (pytest -v -s -m "not Regression")
# -m used to run the tests with multiple tags (pytest -v -s -m  "Regression or Smoke")
# -m used to run the tests with multiple tags (pytest -v -s -m  "Regression and Smoke")
# ********************************************************************************
# to disable warning (--disable-pytest-warnings)
# or register the customised markers to avoid warnings (by creating the .ini file)

import pytest

# Decorator (@here "Regression" is user defined name OR customised markers)

@pytest.mark.Regression
@pytest.mark.Smoke
def test_001_multipleTag():
    print("This is my first test case")

@pytest.mark.Regression
def test_002_multipleTag():
    print("student list is: ")