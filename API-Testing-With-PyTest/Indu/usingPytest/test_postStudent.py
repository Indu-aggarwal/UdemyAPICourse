# -v (verbose) to print all the tests and their pass/fail status
# ********************************************************************************
# -s to print the output on the console
# ********************************************************************************
# -k to run the specific test (-k <name_of_the_test> <folder_name_option>)
# -k to run the specific tests that contains the matching test string (pytest -v -s -k test_002)

def test_001_post_studentId():
    print("This is my first test case")

def test_002_getStudents():
    print("student list is: ")