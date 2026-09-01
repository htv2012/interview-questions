"""
https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/description/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        pytest.param(
            "1 box has 3 blue 4 red 6 green and 12 yellow marbles", True, id="Example 1"
        ),
        pytest.param("hello world 5 x 5", False, id="Example 2"),
        pytest.param(
            "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s",
            False,
            id="Example 3",
        ),
    ],
)
def test_solution(s, expected):
    sol = Solution()
    assert sol.areNumbersAscending(s) == expected
