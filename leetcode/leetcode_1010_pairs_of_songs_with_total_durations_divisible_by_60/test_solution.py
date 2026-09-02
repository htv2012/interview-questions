"""
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "time, expected",
    [
        pytest.param([30, 20, 150, 100, 40], 3, id="Example 1"),
        pytest.param([60, 60, 60], 3, id="Example 2"),
    ],
)
def test_solution(time, expected):
    sol = Solution()
    assert sol.numPairsDivisibleBy60(time) == expected
