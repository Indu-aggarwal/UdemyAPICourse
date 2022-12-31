# -v (verbose) to print all the tests and their pass/fail status
# -s to print the output on the console

import pytest

a = 101

# Decorator
@pytest.mark.skipif(a>100,reason="Skiiping the test - this is just for practice")
def test_001_skipIf():
    print("This is my first test case")

def test_002_skipIf():
    print("student list is: ")