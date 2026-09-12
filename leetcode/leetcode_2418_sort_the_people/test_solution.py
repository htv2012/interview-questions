"""
https://leetcode.com/problems/sort-the-people/
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "names, heights, expected",
    [
        pytest.param(
            ["Mary", "John", "Emma"],
            [180, 165, 170],
            ["Mary", "Emma", "John"],
            id="Example 1",
        ),
        pytest.param(
            ["Alice", "Bob", "Bob"],
            [155, 185, 150],
            ["Bob", "Alice", "Bob"],
            id="Example 2",
        ),
    ],
)
def test_solution(names, heights, expected):
    sol = Solution()
    assert sol.sortPeople(names, heights) == expected
