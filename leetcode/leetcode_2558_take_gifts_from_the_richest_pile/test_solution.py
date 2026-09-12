"""
https://leetcode.com/problems/take-gifts-from-the-richest-pile/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "gifts, k, expected",
    [
        pytest.param([25, 64, 9, 4, 100], 4, 29, id="Example 1"),
        pytest.param([1, 1, 1, 1], 4, 4, id="Example 2"),
    ],
)
def test_solution(gifts, k, expected):
    sol = Solution()
    assert sol.pickGifts(gifts, k) == expected
