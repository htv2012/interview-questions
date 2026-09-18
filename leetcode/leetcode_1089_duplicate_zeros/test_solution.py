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
        pytest.param([], [], id="empty array"),
        pytest.param([1], [1], id="1"),
        pytest.param([0], [0], id="0"),
        pytest.param([0, 1], [0, 0], id="0, 1"),
        pytest.param([1, 0], [1, 0], id="1, 0"),
    ],
)
def test_solution(arr, expected):
    sol = Solution()
    sol.duplicateZeros(arr)
    assert arr == expected
