# In pyTest any files should start with test_ or end with _test
# pyTest method names should start with test_
# Any code should be wrapped in method only
# To execute all the files in a folder in command prompt is : py.test ( gives less information ) . To get more nfo we will give py.test -v -s command
# -k stands for method names executions , -s stands for logs and -v stands fot more information
# To select specfic file command is : py.test filename -v -s
# To select specific methods/testcases : pytest -k (method name or common part of method name) -v -s
# To make a specific tests as a group we can use @pytest.mark.smoke
# To mae specific tests to be sipped @pytest.mark.skip
# In some cases test may pass but in some cases test may fail so avoid error we can use @pytest.mark.xfail which helps to not to include in test cases passed or failed eventhough it executes
# fixture is like testing or arranging pre requisites before actual test execution
# conftest helps us to generalize fixture to all the test cases
# when u define fixure scope to clss only it will reun once before class initialization and at the end
# data driven and parametrization can be done through the return statement in tuple format
import pytest


@pytest.mark.smoke
def test_skp(setup):
    print("Hello")

def test_dhoni_raina():
    print("World !!!")
#parametrization
def test_crossBrowsing(crossBrowser):
    print(crossBrowser)