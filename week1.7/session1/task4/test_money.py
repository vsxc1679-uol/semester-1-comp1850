# Week 1.7, Session 1: Task 4 - unit tests for methods in Money

import pytest

from money import Money

def test_invalid_type_pound():
    with pytest.raises(TypeError) as excinfo:
        Money(1.2, 99)
    assert str(excinfo.value) == "pounds must be an integer"


def test_invalid_value_pound():
    with pytest.raises(ValueError) as excinfo:
        Money(-1, 0)
    assert str(excinfo.value) == "pounds must be >= 0"


def test_add_invalid_type():
    m1 = Money(5, 0)
    with pytest.raises(TypeError) as excinfo:
        m1 + 42
    assert str(excinfo.value) == "other object must be a Money"


def test_invalid_type_pence():
    with pytest.raises(TypeError) as excinfo:
        m1 = Money(0,0.1)
    assert str(excinfo.value) == "pence must be an integer"

test_invalid_type_pence()

def test_invalid_value_pence():
    with pytest.raises(ValueError) as excinfo:
        m1 = Money(0,101)
    assert str(excinfo.value) == "pence must be in range 0-99"

def test_valid_add():
    m1 = Money(5,5)
    m2 = Money(7,50)
    assert str(m1 + m2) == "£12.55"
    # complete the test implementation for
    # valid add between money objects
    # Hint: you can compare using the __str()__ (
    # e.g., str(m1 + m2) == "£2.04"
test_invalid_type_pence()
test_invalid_value_pence()
test_valid_add()