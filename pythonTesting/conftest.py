from typing import List

import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will execute first before actual test")
    yield
    print("I will execute after actual test run")
@pytest.fixture(scope="class")
def dataLoad():
    l=["suneni","Kualayappa","skp@gmail.com"]
    return l

@pytest.fixture(params = [("chrome",'skp','sp@gmail.com'),('Firefox','dhoni','dhoni@gmail.com'),('IE','Virat','virat@gmail.com')])
def crossBrowser(request):
    return request.param
