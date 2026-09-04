"""
https://leetcode.com/problems/strong-password-checker-ii/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param("IloveLe3tcode!", True, id="Example 1"),
        pytest.param("Me+You--IsMyDream", False, id="Example 2"),
        pytest.param("1aB!", False, id="Example 3"),
        pytest.param("1aB!cc", False, id="repeated char"),
        pytest.param("11A!A!Aa", False, id="repeat digit"),
    ],
)
def test_solution(password, expected):
    sol = Solution()
    assert sol.strongPasswordCheckerII(password) == expected
