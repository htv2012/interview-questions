# Test convert from infix to RPN: infix_to_rpn()
import operator

import pytest

from solution import evaluate_rpn


@pytest.mark.parametrize(
    "rpn, expected",
    [
        pytest.param([1, 1, operator.add], 2, id="example 1"),
    ],
)
def test_evaluate_rpn(rpn, expected):
    assert evaluate_rpn(rpn) == expected
