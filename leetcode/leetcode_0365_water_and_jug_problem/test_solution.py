"""
https://leetcode.com/problems/water-and-jug-problem/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "x, y, target, expected",
    [
        pytest.param(3, 5, 4, True, id="Example 1"),
        pytest.param(2, 6, 5, False, id="Example 2"),
        pytest.param(1, 2, 3, True, id="Example 3"),
        pytest.param(1, 10, 8, True, id="my 1"),
        pytest.param(1, 2, 4, False, id="target is too big"),
    ],
)
def test_solution(x, y, target, expected):
    sol = Solution()
    assert sol.canMeasureWater(x, y, target) is expected
