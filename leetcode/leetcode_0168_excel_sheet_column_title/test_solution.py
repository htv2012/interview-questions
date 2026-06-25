"""
https://leetcode.com/problems/excel-sheet-column-title
"""

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.convertToTitle


@pytest.mark.parametrize(
    "columnNumber, expected",
    [
        (1, "A"),
        (25, "Y"),
        (26, "Z"),
        (27, "AA"),
        (28, "AB"),
        (51, "AY"),
        (52, "AZ"),
        (53, "BA"),
        (104, "CZ"),
        (701, "ZY"),
        (702, "ZZ"),
        (1025971428, "CHICKEN"),
        (2441, "COW"),
        (3932115, "HORSE"),
        (112042, "FISH"),
        (3929017, "HONDA"),
        (244932221, "TOYOTA"),
    ],
)
def test_solution(fut, columnNumber, expected):
    assert fut(columnNumber) == expected
