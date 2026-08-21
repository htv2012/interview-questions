# Test convert from infix to RPN: infix_to_rpn()
import operator

import pytest

from solution import change_sign, infix_to_rpn


@pytest.mark.parametrize(
    "infix, expected",
    [
        pytest.param("2 + 3", [2, 3, operator.add], id="simple add"),
        pytest.param("5 - 1 + 9", [5, 1, operator.sub, 9, operator.add], id="3 terms"),
        pytest.param("-15", [15, change_sign], id="unary minus at start"),
        pytest.param(
            "15 + -5",
            [15, 5, change_sign, operator.add],
            id="unary minus follows a plus",
        ),
        pytest.param("1 + 1", [1, 1, operator.add], id="example 1"),
        pytest.param("2-1 + 2", [2, 1, operator.sub, 2, operator.add], id="example 2"),
        pytest.param(
            "5 + (-1 + 3)",
            [5, 1, change_sign, 3, operator.add, operator.add],
            id="unary minus follows a left paren",
        ),
        pytest.param("1+5-4", [1, 5, operator.add, 4, operator.sub], id="wrong 1"),
    ],
)
def test_infix_to_rpn(infix, expected):
    assert infix_to_rpn(infix) == expected
