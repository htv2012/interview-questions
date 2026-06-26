"""
https://leetcode.com/problems/transform-array-by-parity
"""

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.transformArray


@pytest.mark.parametrize(
    "nums,expected",
    [
        pytest.param([4, 3, 2, 1], [0, 0, 1, 1], id="example1"),
        pytest.param([1, 5, 1, 4, 2], [0, 0, 1, 1, 1], id="example2"),
        pytest.param([], [], id="empty"),
        pytest.param([1], [1], id="[1]"),
    ],
)
def test_solution(fut, nums, expected):
    assert fut(nums) == expected
