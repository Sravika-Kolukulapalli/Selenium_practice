
import pytest
@pytest.fixture()  #decorator
def setup():
    print("Launching browser")#Execute once before every test method
    yield
    print("Closing browser")#Execute once after every test method