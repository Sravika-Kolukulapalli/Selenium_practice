import pytest

class TestClass:
    @pytest.mark.run(order=3)
    def test_methodC(self):
        print("This is test method C")
    @pytest.mark.run(order=4)
    def test_methodD(self):
        print("This is test method D")
    @pytest.mark.run(order=5)
    def test_methodE(self):
        print("This is test method E")
    @pytest.mark.run(order=1)
    def test_methodA(self):
        print("This is test method A ")
    @pytest.mark.run(order=2)
    def test_methodB(self):
        print("This is test method B")
