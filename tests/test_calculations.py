import pytest
from app.calculation.calculation import Calculation
from app.calculation.factory import CalculationFactory
from app.operation.operations import Add


def test_calculation_result():
    calc = Calculation(2, 3, Add())
    assert calc.result() == 5


def test_factory_create():
    calc = CalculationFactory.create("add", 1, 2)
    assert calc.result() == 3


def test_factory_invalid():
    with pytest.raises(ValueError):
        CalculationFactory.create("bad", 1, 2)
