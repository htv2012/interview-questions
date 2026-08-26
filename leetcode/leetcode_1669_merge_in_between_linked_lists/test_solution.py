"""
https://leetcode.com/problems/merge-in-between-linked-lists/
"""

import pytest
from list_node import build, verify_values

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.mergeInBetween


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["list1"],
        kwargs["a"],
        kwargs["b"],
        kwargs["list2"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "list1, a, b, list2, expected",
    [
        tc(
            test_id="Example 1",
            list1=[10, 1, 13, 6, 9, 5],
            a=3,
            b=4,
            list2=[1000000, 1000001, 1000002],
            expected=[10, 1, 13, 1000000, 1000001, 1000002, 5],
        ),
        tc(
            test_id="Example 2",
            list1=[0, 1, 2, 3, 4, 5, 6],
            a=2,
            b=5,
            list2=[1000000, 1000001, 1000002, 1000003, 1000004],
            expected=[0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6],
        ),
        tc(
            test_id="wrong 1",
            list1=[0, 1, 2],
            a=1,
            b=1,
            list2=[1000000, 1000001, 1000002, 1000003],
            expected=[0, 1000000, 1000001, 1000002, 1000003, 2],
        ),
    ],
)
def test_solution(fut, list1, a, b, list2, expected):
    assert len(list1) >= 3, "Pre-condition: list1 has at least 3 nodes"
    assert len(list2) > 0, "Pre-condition: list2 has at least 1 node"
    assert 1 <= a < len(list1), "Pre-condition: a must be in range"
    assert 1 <= b < len(list1), "Pre-condition: b must be in range"

    head1 = build(list1)
    head2 = build(list2)
    actual = fut(head1, a, b, head2)
    assert verify_values(actual, expected)
