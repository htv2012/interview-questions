"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "numbers, target, expected",
    [
        pytest.param([2, 7, 11, 15], 9, [1, 2], id="Example 1"),
        pytest.param([2, 3, 4], 6, [1, 3], id="Example 2"),
        pytest.param([-1, 0], -1, [1, 2], id="Example 3"),
    ],
)
def test_solution(numbers, target, expected):
    sol = Solution()
    assert sol.twoSum(numbers, target) == expected
