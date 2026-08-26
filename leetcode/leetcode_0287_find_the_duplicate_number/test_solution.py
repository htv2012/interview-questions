"""
https://leetcode.com/problems/find-the-duplicate-number/description/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        pytest.param([1, 3, 4, 2, 2], 2, id="Example 1"),
        pytest.param([3, 1, 3, 4, 2], 3, id="Example 2"),
        pytest.param([3, 3, 3, 3, 3], 3, id="Example 3"),
    ],
)
def test_solution(nums, expected):
    sol = Solution()
    assert sol.findDuplicate(nums) == expected
