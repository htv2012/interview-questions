"""
https://leetcode.com/problems/convert-to-base-2/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "n, expected",
    [
        pytest.param(2, "110", id="Example 1"),
        pytest.param(3, "111", id="Example 2"),
        pytest.param(4, "100", id="Example 3"),
        pytest.param(-8, "1000", id="-8"),
    ],
)
def test_solution(n, expected):
    sol = Solution()
    assert sol.baseNeg2(n) == expected
