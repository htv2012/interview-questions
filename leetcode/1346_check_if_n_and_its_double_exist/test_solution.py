import logging

import pytest


@pytest.mark.parametrize(
    ["arr", "expected"],
    [
        pytest.param([10, 2, 5, 3], True, id="Example 1"),
        pytest.param([3, 1, 7, 11], False, id="Example 2"),
        pytest.param([-2, 0, 10, -19, 4, 6, -8], False, id="wrong 1"),
        pytest.param([1, 3, 5, 7], False, id="my 1"),
        pytest.param([], False, id="empty"),
    ],
)
def test_solution(fut, arr, expected):
    logging.debug("arr=%r", arr)
    logging.debug("expected=%r", expected)
    actual = fut(arr)
    logging.debug("actual=%r", actual)
    assert actual is expected
