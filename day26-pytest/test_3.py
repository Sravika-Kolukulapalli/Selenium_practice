import pytest
#1)fixtures----

class TestClass:
    @pytest.fixture()  #decorator
    def setup(self):
        print("Launching browser")#Execute once before every test method
        yield
        print("Closing browser")#Execute once after every test method
    def test_login(self,setup):
        print("This is login test")

    def test_Search(self,setup):
        print("This is search test")

    def test_Advancedsearch(self,setup):
        print("This is advanced search test")
