import pytest
from calc import add, divide, average, clamp
def test_add(): assert add(2, 3) == 5
def test_divide(): assert divide(6, 3) == 2
def test_divide_zero():
    with pytest.raises(ValueError): divide(1, 0)
def test_average(): assert average([1, 2, 3]) == 2
def test_clamp(): assert clamp(15, 0, 10) == 10
