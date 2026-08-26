# test_fraction.py

import pytest

from solution import Fraction


@pytest.mark.parametrize(
    "args, expected_num, expected_dem",
    [
        pytest.param((2, 4), 2, 4, id="no sign"),
        pytest.param((-2, 4), -2, 4, id="negative"),
    ],
)
def test_create(args, expected_num, expected_dem):
    actual = Fraction(*args)
    assert actual.num == expected_num
    assert actual.dem == expected_dem


@pytest.mark.parametrize(
    "args, expected",
    [
        pytest.param((2, 4), "2/4", id="no sign"),
        pytest.param((-2, 4), "-2/4", id="negative"),
    ],
)
def test_str(args, expected):
    actual = Fraction(*args)
    assert str(actual) == expected


@pytest.mark.parametrize(
    "fraction, expected_num, expected_dem",
    [
        pytest.param(Fraction(2, 8), 1, 4, id="simplifiable, positive"),
        pytest.param(Fraction(-4, 16), -1, 4, id="simplifiable, negative"),
        pytest.param(Fraction(1, 3), 1, 3, id="non-simplifiable, positive"),
        pytest.param(Fraction(-1, 3), -1, 3, id="non-simplifiable, negative"),
        pytest.param(Fraction(0, 5), 0, 1, id="zero"),
    ],
)
def test_reduce(fraction, expected_num, expected_dem):
    fraction.reduce()
    assert fraction.num == expected_num
    assert fraction.dem == expected_dem


@pytest.mark.parametrize(
    "fraction1, fraction2, expected_num, expected_dem",
    [
        pytest.param(Fraction(1, 3), Fraction(1, 5), 8, 15, id="1/3 + 1/5"),
        pytest.param(Fraction(1, 3), Fraction(-1, 5), 2, 15, id="1/3 - 1/5"),
        pytest.param(Fraction(2, 3), Fraction(-1, 6), 1, 2, id="2/3 - 1/6"),
        pytest.param(Fraction(1, 3), Fraction(-1, 3), 0, 1, id="1/3 - 1/3"),
    ],
)
def test_add(fraction1, fraction2, expected_num, expected_dem):
    actual = fraction1 + fraction2
    assert actual.num == expected_num
    assert actual.dem == expected_dem


@pytest.mark.parametrize(
    "fraction1, fraction2, expected",
    [
        pytest.param(Fraction(1, 3), Fraction(1, 3), True, id="identical"),
        pytest.param(Fraction(4, 8), Fraction(5, 10), True, id="same after reducing"),
        pytest.param(Fraction(4, 8), Fraction(6, 10), False, id="not same"),
    ],
)
def test_equal(fraction1, fraction2, expected):
    assert (fraction1 == fraction2) is expected
