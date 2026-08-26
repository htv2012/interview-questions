"""
https://leetcode.com/problems/add-strings
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        pytest.param("11", "123", "134", id="Example 1"),
        pytest.param("456", "77", "533", id="Example 2"),
        pytest.param("0", "0", "0", id="Example 3"),
    ],
)
def test_solution(num1, num2, expected):
    sol = Solution()
    assert sol.addStrings(num1, num2) == expected
