"""
https://leetcode.com/problems/move-zeroes/
"""

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.moveZeroes


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
        tc(test_id="Example 1", nums=[0, 1, 0, 3, 12], expected=[1, 3, 12, 0, 0]),
        tc(test_id="Example 2", nums=[0], expected=[0]),
        tc(test_id="wrong 1", nums=[1], expected=[1]),
        tc(test_id="wrong 2", nums=[1, 0, 1], expected=[1, 1, 0]),
        tc(test_id="all zeros", nums=[0, 0, 0, 0], expected=[0, 0, 0, 0]),
        tc(test_id="lots of z", nums=[1, 0, 2, 0, 3, 0], expected=[1, 2, 3, 0, 0, 0]),
        tc(test_id="tons of zeros", nums=[0] * 10000 + [1], expected=[1] + [0] * 10000),
    ],
)
def test_solution(fut, nums, expected):
    fut(nums)
    assert nums == expected
