import pytest


class TestClass:
    def test_LoginByEmail(self):
        print("This is login by email")
        assert True == True

    def test_LoginByFacebook(self):
        print("This is login by facebook")
        assert True == True

    def test_LoginByTwitter(self):
        print("This is login by twitter")
        assert True == True
    @pytest.mark.skip
    def test_SignUpByEmail(self):
        print("This is signup by email")
        assert True == True
    @pytest.mark.skip
    def test_SignUpByFacebook(self):
        print("This is signup by facebook")
        assert True == True
    @pytest.mark.skip
    def test_SignUpByTwitter(self):
        print("This is signup by twitter")
        assert True == True
