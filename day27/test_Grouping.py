import pytest


class TestClass:
    @pytest.mark.sanity
    def test_LoginByEmail(self):
        print("This is login by email")
        assert True == True

    @pytest.mark.sanity
    def test_LoginByFacebook(self):
        print("This is login by facebook")
        assert True == True

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_LoginByTwitter(self):
        print("This is login by twitter")
        assert True == True


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_SignUpByEmail(self):
        print("This is signup by email")
        assert True == True

    @pytest.mark.regression
    def test_SignUpByFacebook(self):
        print("This is signup by facebook")
        assert True == True

    @pytest.mark.regression
    def test_SignUpByTwitter(self):
        print("This is signup by twitter")
        assert True == True


#pytest -v -s -m "sanity"  day27/test_Grouping.py---= 4 passed, 2 deselected in 0.04s ==
# pytest -v -s -m "regression"  day27/test_Grouping.py---== 4 passed, 2 deselected in 0.03s
# pytest -v -s -m "sanity and regression"  day27/test_Grouping.py--- 2 passed, 4 deselected in 0.02s =
# pytest -v -s -m "not regression"  day27/test_Grouping.py-----2 passed, 4 deselected in 0.02s
# pytest -v -s -m "not sanity"  day27/test_Grouping.py---- 2 passed, 4 deselected in 0.02s





