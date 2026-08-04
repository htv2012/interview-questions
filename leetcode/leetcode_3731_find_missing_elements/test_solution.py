"""
https://leetcode.com/problems/find-missing-elements/
"""

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.findMissingElements


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
            nums=[1, 4, 2, 5],
            expected=[3],
        ),
        tc(
            test_id="Example 2",
            nums=[7, 8, 6, 9],
            expected=[],
        ),
        tc(
            test_id="Example 3",
            nums=[5, 1],
            expected=[2, 3, 4],
        ),
    ],
)
def test_solution(fut, nums, expected):
    assert fut(nums) == expected
