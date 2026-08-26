"""
https://leetcode.com/problems/base-7/description/
"""

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.convertToBase7


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["num"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "num, expected",
    [
        tc(
            test_id="Example 1",
            num=100,
            expected="202",
        ),
        tc(
            test_id="Example 2",
            num=-7,
            expected="-10",
        ),
        (-14, "-20"),
        (0, "0"),
    ],
)
def test_solution(fut, num, expected):
    assert fut(num) == expected
