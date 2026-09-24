"""
https://leetcode.com/problems/stock-price-fluctuation/
"""

import pytest

from solution import StockPrice


@pytest.mark.parametrize(
    "action_list, args_list, expected_list",
    [
        pytest.param(
            [
                "StockPrice",
                "update",
                "update",
                "current",
                "maximum",
                "update",
                "maximum",
                "update",
                "minimum",
            ],
            [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []],
            [None, None, None, 5, 10, None, 5, None, 2],
            id="Example 1",
        ),
    ],
)
def test_solution(action_list, args_list, expected_list):
    sp = StockPrice()

    for action, args, expected in zip(action_list, args_list, expected_list):
        if action == "StockPrice":
            continue

        method = getattr(sp, action)
        actual = method(*args)
        assert actual == expected
