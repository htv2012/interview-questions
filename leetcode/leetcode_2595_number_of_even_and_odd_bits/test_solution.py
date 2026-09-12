"""
https://leetcode.com/problems/number-of-even-and-odd-bits/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "n, expected",
    [
        pytest.param(50, [1, 2], id="Example 1"),
        pytest.param(2, [0, 1], id="Example 2"),
    ],
)
def test_solution(n, expected):
    sol = Solution()
    assert sol.evenOddBit(n) == expected
