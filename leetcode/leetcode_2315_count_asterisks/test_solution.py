"""
https://leetcode.com/problems/count-asterisks/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        pytest.param("l|*e*et|c**o|*de|", 2, id="Example 1"),
        pytest.param("iamprogrammer", 0, id="Example 2"),
        pytest.param("yo|uar|e**|b|e***au|tifu|l", 5, id="Example 3"),
    ],
)
def test_solution(s, expected):
    sol = Solution()
    assert sol.countAsterisks(s) == expected
