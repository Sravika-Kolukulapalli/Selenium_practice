import pytest

class TestClass:
    @pytest.mark.parametrize('num1,num2',[(1,1),(2,4),(3,3),(4,6),(5,5)])
    def test_calculation(self,num1,num2):
        assert num1==num2