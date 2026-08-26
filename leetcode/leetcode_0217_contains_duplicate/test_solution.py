"""
https://leetcode.com/problems/contains-duplicate/
"""

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.containsDuplicate


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
            test_id="Example 1",
            nums=[1, 2, 3, 1],
            expected=True,
        ),
        tc(
            test_id="Example 2",
            nums=[1, 2, 3, 4],
            expected=False,
        ),
        tc(
            test_id="Example 3",
            nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
            expected=True,
        ),
    ],
)
def test_solution(fut, nums, expected):
    assert fut(nums) == expected
