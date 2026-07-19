"""
https://leetcode.com/problems/summary-ranges/
"""

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.summaryRanges


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["nums"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "nums, expected",
    [
        tc(
            test_id="Example 1", nums=[0, 1, 2, 4, 5, 7], expected=["0->2", "4->5", "7"]
        ),
        tc(
            test_id="Example 2",
            nums=[0, 2, 3, 4, 6, 8, 9],
            expected=["0", "2->4", "6", "8->9"],
        ),
        tc(test_id="empty", nums=[], expected=[]),
        tc(test_id="single entry", nums=[9999], expected=["9999"]),
    ],
)
def test_solution(fut, nums, expected):
    assert fut(nums) == expected
