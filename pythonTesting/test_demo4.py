import pytest

from pythonTesting.BaseClass import BaseClass
from pythonTesting.conftest import dataLoad


@pytest.mark.usefixtures('dataLoad')
class Test2(BaseClass):
    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[1])
        log.info(dataLoad[2])
