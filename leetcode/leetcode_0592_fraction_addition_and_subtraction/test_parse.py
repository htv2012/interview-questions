import pytest

from solution import Fraction, parse_expression


@pytest.mark.parametrize(
    "expression, expected",
    [
        pytest.param("4/5", [Fraction(4, 5)], id="single, positive"),
        pytest.param("-2/7", [Fraction(-2, 7)], id="single, negative"),
        pytest.param("3/7-2/15", [Fraction(3, 7), Fraction(-2, 15)], id="3/7-2/15"),
    ],
)
def test_parse(expression, expected):
    actual = parse_expression(expression)
    assert actual == expected
