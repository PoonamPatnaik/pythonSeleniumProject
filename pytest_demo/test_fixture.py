import pytest


@pytest.fixture()
def setup():
    print("setup")
    yield
    print("teardown")
def test_ficture(setup):
    print("Fixture execeution")