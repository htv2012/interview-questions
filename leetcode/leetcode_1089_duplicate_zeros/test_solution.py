"""
https://leetcode.com/problems/duplicate-zeros/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "arr, expected",
    [
        pytest.param(
            [1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4], id="Example 1"
        ),
        pytest.param([1, 2, 3], [1, 2, 3], id="Example 2"),
        pytest.param([1, 0, 2, 0, 3], [1, 0, 0, 2, 0], id="spill over"),
    ],
)
def test_solution(arr, expected):
    sol = Solution()
    sol.duplicateZeros(arr)
    assert arr == expected
