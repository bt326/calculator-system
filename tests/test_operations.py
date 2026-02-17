import pytest
from app.operation.operations import Add, Subtract, Multiply, Divide


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(a, b, expected):
    assert Add().execute(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (0, 5, -5),
    (-2, -2, 0)
])
def test_subtract(a, b, expected):
    assert Subtract().execute(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (5, 0, 0),
    (-2, 4, -8)
])
def test_multiply(a, b, expected):
    assert Multiply().execute(a, b) == expected


def test_divide():
    assert Divide().execute(6, 2) == 3


def test_divide_by_zero():
    with pytest.raises(ValueError):
        Divide().execute(5, 0)
def test_base_operation():

    from app.operation.operations import Operation

    op = Operation()

    try:
        op.execute(1, 2)
        assert False
    except NotImplementedError:
        assert True
