"""
https://leetcode.com/problems/guess-number-higher-or-lower/
"""

import pytest

import solution


@pytest.mark.parametrize(
    "n, pick",
    [(10, 6), (1, 1), (2, 1)],
)
def test_solution(n, pick):
    fut = solution.Solution().guessNumber
    solution.pick = pick
    assert fut(n) == pick
