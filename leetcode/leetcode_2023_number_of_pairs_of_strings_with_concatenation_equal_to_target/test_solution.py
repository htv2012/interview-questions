"""
https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        pytest.param(["777", "7", "77", "77"], "7777", 4, id="Example 1"),
        pytest.param(["123", "4", "12", "34"], "1234", 2, id="Example 2"),
        pytest.param(["1", "1", "1"], "11", 6, id="Example 3"),
    ],
)
def test_solution(nums, target, expected):
    sol = Solution()
    assert sol.numOfPairs(nums, target) == expected
