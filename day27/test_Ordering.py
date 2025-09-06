import pytest

class TestClass:
    @pytest.mark.third
    def test_methodC(self):
        print("This is test method C")
    @pytest.mark.fourth
    def test_methodD(self):
        print("This is test method D")
    @pytest.mark.fifth
    def test_methodE(self):
        print("This is test method E")
    @pytest.mark.first
    def test_methodA(self):
        print("This is test method A ")
    @pytest.mark.second
    def test_methodB(self):
        print("This is test method B")
