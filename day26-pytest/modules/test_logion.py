#test_login

import pytest

class TestLogion:
    def test_LoginByEmail(self,setup):
        print("This is login by email")
        assert True==True

    def test_LoginByFacebook(self,setup):
        print("This is login by facebook")
        assert True == True

    def test_LoginByTwitter(self,setup):
        print("This is login by twitter")
        assert True == True
