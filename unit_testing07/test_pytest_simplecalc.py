# PyTest
from unit_testing07.simplecalc import SimpleCalc
import pytest


@pytest.fixture
def calc():
    return SimpleCalc()


#  what this allows you to do is:
def test_calc_add1(calc):
    assert calc.add(2, 6) == 8
#  and you don't have to specify calc = SimpleCalc() every time in a test


def test_calc_add():
    calc = SimpleCalc()
    assert calc.add(2, 6) == 8


def test_calc_subtract():
    calc = SimpleCalc()
    assert calc.subtract(6, 2) == 4


def test_calc_multiply():
    calc = SimpleCalc()
    assert pytest.approx(calc.multiply(0.4, -80.9)) == -32.36
    #  to solve: import pytest
    #  instead of assert, use assert pytest.approx().
    #  for degree of approx, use ptest.approx(()000.1)


def test_calc_divide():
    calc = SimpleCalc()
    assert calc.divide(6, 3) == 2

#  pytest -v will enter verbose mode for more info.


def test_calc_divive_by_zero_raises_error():
    calc = SimpleCalc()
    # we need a context manager to solve this. i.e. 'with'
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)
    #  with means that 'with' something going on, something else should happen
    #  pytest.raises() checks for a specific issue/error; ZeroDivisionError is prebuilt into py