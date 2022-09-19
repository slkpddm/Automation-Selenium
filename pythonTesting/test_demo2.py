import pytest

@pytest.mark.xfail
def test_dhoni():
    assert "skp" == "Dhoni" , "Test case failed"
@pytest.mark.skip
def test_dhoni7(setup):
    print("Dhoni")
@pytest.mark.smoke
def test_virat():
    assert "virat" == "anusha" , "Gendor difference"
