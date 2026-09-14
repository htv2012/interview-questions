"""
https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "rectangles, expected",
    [
        pytest.param([[4, 8], [3, 6], [10, 20], [15, 30]], 6, id="Example 1"),
        pytest.param([[4, 5], [7, 8]], 0, id="Example 2"),
    ],
)
def test_solution(rectangles, expected):
    sol = Solution()
    assert sol.interchangeableRectangles(rectangles) == expected
