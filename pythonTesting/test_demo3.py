import pytest


@pytest.mark.usefixtures("setup")
class Test():
     def test_demo1(self):
         print("test1")
     def test_demo2(self):
         print("demo2")
     def test_demo3(self):
         assert 1==3,"1 not eqaul to 3"
