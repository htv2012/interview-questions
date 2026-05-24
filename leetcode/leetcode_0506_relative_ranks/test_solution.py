"""
https://leetcode.com/problems/relative-ranks/
"""

import pytest

from solution import find_relative_ranks


@pytest.mark.parametrize(
    ["score", "expected"],
    [
        pytest.param(
            [5, 4, 3, 2, 1],
            ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"],
            id="Example 1",
        ),
        pytest.param(
            [10, 3, 8, 9, 4],
            ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"],
            id="Example 2",
        ),
        pytest.param([1], ["Gold Medal"], id="single contestant"),
        pytest.param([1, 2], ["Silver Medal", "Gold Medal"], id="two contestants"),
        pytest.param(
            [129, 280, 547, 739, 847, 403, 746, 149, 879, 35],
            [
                "9",
                "7",
                "5",
                "4",
                "Silver Medal",
                "6",
                "Bronze Medal",
                "8",
                "Gold Medal",
                "10",
            ],
            id="longer list",
        ),
    ],
)
def test_solution(score, expected):
    assert find_relative_ranks(score) == expected
