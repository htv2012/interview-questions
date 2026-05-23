"""
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
"""

import pytest


@pytest.mark.parametrize(
    ["nums", "expected"],
    [
        pytest.param([3, 4, 5, 1, 2], True, id="example 1"),
        pytest.param([2, 1, 3, 4], False, id="example 2"),
        pytest.param([1, 2, 3], True, id="example 3"),
        pytest.param([1], True, id="one element"),
        pytest.param([], True, id="empty list"),
    ],
)
def test_solution(fut, nums, expected):
    assert fut(nums) == expected
