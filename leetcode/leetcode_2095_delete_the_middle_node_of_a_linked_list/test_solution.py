"""
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
"""

import pytest
from list_node import build, verify_values

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.deleteMiddle


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["values"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "values, expected",
    [
        tc(
            test_id="Example 1",
            values=[1, 3, 4, 7, 1, 2, 6],
            expected=[1, 3, 4, 1, 2, 6],
        ),
        tc(
            test_id="Example 2",
            values=[1, 2, 3, 4],
            expected=[1, 2, 4],
        ),
        tc(
            test_id="Example 3",
            values=[2, 1],
            expected=[2],
        ),
        tc(
            test_id="single node",
            values=[1],
            expected=[],
        ),
        tc(
            test_id="empty",
            values=[],
            expected=[],
        ),
    ],
)
def test_solution(fut, values, expected):
    head = build(values)
    actual = fut(head)
    assert verify_values(actual, expected)
