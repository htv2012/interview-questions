"""
https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
"""

import list_node
import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.modifiedList


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["nums"],
        kwargs["list_values"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "nums, list_values, expected",
    [
        tc(
            test_id="Example 1",
            nums=[1, 2, 3],
            list_values=[1, 2, 3, 4, 5],
            expected=[4, 5],
        ),
        tc(
            test_id="Example 2",
            nums=[1],
            list_values=[1, 2, 1, 2, 1, 2],
            expected=[2, 2, 2],
        ),
        tc(
            test_id="Example 3",
            nums=[5],
            list_values=[1, 2, 3, 4],
            expected=[1, 2, 3, 4],
        ),
    ],
)
def test_solution(fut, nums, list_values, expected):
    head = list_node.build(list_values)
    actual = fut(nums, head)
    assert list_node.verify_values(actual, expected)
