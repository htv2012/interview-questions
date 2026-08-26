"""
https://leetcode.com/problems/fraction-addition-and-subtraction/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "expression, expected",
    [
        pytest.param("-1/2+1/2", "0/1", id="Example 1"),
        pytest.param("-1/2+1/2+1/3", "1/3", id="Example 2"),
        pytest.param("1/3-1/2", "-1/6", id="Example 3"),
    ],
)
def test_solution(expression, expected):
    sol = Solution()
    assert sol.fractionAddition(expression) == expected
