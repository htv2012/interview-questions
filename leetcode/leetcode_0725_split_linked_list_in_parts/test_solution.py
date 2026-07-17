"""
https://leetcode.com/problems/split-linked-list-in-parts/
"""

import pytest
from list_node import ListNode, verify_values

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.splitListToParts


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["head"],
        kwargs["k"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "head, k, expected",
    [
        tc(
            test_id="Example 1",
            head=[1, 2, 3],
            k=5,
            expected=[[1], [2], [3], [], []],
        ),
        tc(
            test_id="Example 2",
            head=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            k=3,
            expected=[[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]],
        ),
        tc(test_id="empty", head=[], k=3, expected=[[], [], []]),
        tc(test_id="k=1", head=[1, 2, 3], k=1, expected=[[1, 2, 3]]),
    ],
)
def test_solution(fut, head, k, expected):
    head = ListNode.from_iterable(head)
    actual = fut(head, k)

    assert len(actual) == len(expected), "number of lists returned mismatched"
    for sub_list, expected_values in zip(actual, expected):
        assert verify_values(sub_list, expected_values)
