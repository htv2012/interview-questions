"""
https://leetcode.com/problems/find-original-array-from-doubled-array/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "changed, expected",
    [
        pytest.param([1, 3, 4, 2, 6, 8], [1, 3, 4], id="Example 1"),
        pytest.param([6, 3, 0, 1], [], id="Example 2"),
        pytest.param([1], [], id="Example 3"),
    ],
)
def test_solution(changed, expected):
    sol = Solution()
    assert sol.findOriginalArray(changed) == expected
