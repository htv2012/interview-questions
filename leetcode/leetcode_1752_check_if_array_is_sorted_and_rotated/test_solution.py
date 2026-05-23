"""
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
"""

import pytest


@pytest.mark.parametrize(
    ['nums', 'expected'],    [
        pytest.param([3, 4, 5, 1, 2], True, id='Example 1'),
        pytest.param([2, 1, 3, 4], False, id='Example 2'),
        pytest.param([1, 2, 3], True, id='Example 3'),
    ],
)
def test_solution(fut, nums, expected):
    assert fut(nums) == expected