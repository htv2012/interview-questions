"""
https://leetcode.com/problems/remove-linked-list-elements/
"""

import pytest
from list_node import ListNode, verify_values

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.removeElements


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["head"],
        kwargs["val"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "head, val, expected",
    [
        tc(
            test_id="Example 1",
            head=[1, 2, 6, 3, 4, 5, 6],
            val=6,
            expected=[1, 2, 3, 4, 5],
        ),
        tc(test_id="Example 2", head=[], val=1, expected=[]),
        tc(test_id="Example 3", head=[7, 7, 7, 7], val=7, expected=[]),
        tc(test_id="all but one", head=[1, 2, 1, 1], val=1, expected=[2]),
        tc(test_id="val not found", head=[1, 2, 3, 4], val=5, expected=[1, 2, 3, 4]),
        tc(
            test_id="load, not found", head=[1] * 100_000, val=2, expected=[1] * 100_000
        ),
        tc(test_id="load, found", head=[1] * 100_000, val=1, expected=[]),
    ],
)
def test_solution(fut, head, val, expected):
    input_list = ListNode.from_iterable(head)

    actual = fut(input_list, val)
    assert verify_values(actual, expected)
