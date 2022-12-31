# -v (verbose) to print all the tests and their pass/fail status
# -s to print the output on the console

import pytest

# Decorator
@pytest.mark.skip("Skiiping the test - this is just for practice")
def test_001_skip():
    print("This is my first test case")

def test_002_skip():
    print("student list is: ")