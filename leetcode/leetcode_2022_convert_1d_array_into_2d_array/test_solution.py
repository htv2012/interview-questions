"""
https://leetcode.com/problems/convert-1d-array-into-2d-array/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "original, m, n, expected",
    [
        pytest.param([1, 2, 3, 4], 2, 2, [[1, 2], [3, 4]], id="Example 1"),
        pytest.param([1, 2, 3], 1, 3, [[1, 2, 3]], id="Example 2"),
        pytest.param([1, 2], 1, 1, [], id="Example 3"),
    ],
)
def test_solution(original, m, n, expected):
    sol = Solution()
    assert sol.construct2DArray(original, m, n) == expected
