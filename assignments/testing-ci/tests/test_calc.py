import pytest

from calc import add, sub, mul, div


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 5, 4),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected


def test_sub():
    assert sub(10, 3) == 7


def test_mul():
    assert mul(4, 3) == 12


def test_div():
    assert div(9, 3) == 3


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)
