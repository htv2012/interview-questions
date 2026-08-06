"""
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
"""

import pytest
from list_node import build, verify_values

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.swapNodes


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["list_values"],
        kwargs["k"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "list_values, k, expected",
    [
        tc(
            test_id="Example 1",
            list_values=[1, 2, 3, 4, 5],
            k=2,
            expected=[1, 4, 3, 2, 5],
        ),
        tc(
            test_id="Example 2",
            list_values=[7, 9, 6, 6, 7, 8, 3, 0, 9, 5],
            k=5,
            expected=[7, 9, 6, 6, 8, 7, 3, 0, 9, 5],
        ),
        tc(
            test_id="same node",
            list_values=list(range(9)),
            k=5,
            expected=list(range(9)),
        ),
        tc(test_id="single node", list_values=[9], k=1, expected=[9]),
        tc(
            test_id="adjacent nodes",
            list_values=[1, 2, 3, 4, 5, 6],
            k=4,
            expected=[1, 2, 4, 3, 5, 6],
        ),
    ],
)
def test_solution(fut, list_values, k, expected):
    head = build(list_values)
    actual = fut(head, k)
    assert verify_values(actual, expected)
