import pytest
#1)fixtures----

class TestClass:
    @pytest.fixture()  #decorator
    def setup(self):
        print("Launching browser")
        print("Open application")
    def test_login(self,setup):
        print("This is login test")

    def test_Search(self,setup):
        print("This is search test")

    def test_Advancedsearch(self,setup):
        print("This is advanced search test")
