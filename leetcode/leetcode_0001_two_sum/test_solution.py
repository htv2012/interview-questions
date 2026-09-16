"""
https://leetcode.com/problems/two-sum/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        pytest.param([2, 7, 11, 15], 9, [0, 1], id="Example 1"),
        pytest.param([3, 2, 4], 6, [1, 2], id="Example 2"),
        pytest.param([3, 3], 6, [0, 1], id="Example 3"),
    ],
)
def test_solution(nums, target, expected):
    sol = Solution()
    assert sol.twoSum(nums, target) == expected
