#  TDD and Unit Tests:

import pytest

from unit_testing07.rectangle import Rectangle, Square


@pytest.fixture
def rect():
    return Rectangle(5, 4)

# @pytest.fixture
# def sq():
#     return Square(5)


def test_get_area(rect):
    assert rect.get_area() == 20


def test_get_perimeter(rect):
    assert rect.get_perimeter() == 18


@pytest.fixture
def sq():
    return Square(5)

def test_get_area_sq(sq):
    assert sq.get_area() == 25


def test_get_perimeter_sq(sq):
    assert sq.get_perimeter() == 20


def test_get_number_enclosing(sq):
    assert sq.get_number_enclosing(4.0) == 1