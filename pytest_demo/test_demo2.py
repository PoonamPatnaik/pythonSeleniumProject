import pytest

@pytest.mark.smoke
def test_demo_case():
    print("TC2 Demo fail")
    a=2
    b= 5
    assert a == b
def test_credit_case():
    print("TC credit pass")