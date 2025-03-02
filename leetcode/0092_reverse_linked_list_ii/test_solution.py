#!/usr/bin/env python3
import pytest
from list_node import ListNode


@pytest.mark.parametrize(
    "head, left, right, expected",
    [
        pytest.param([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5], id="example 1"),
        pytest.param([5], 1, 1, [5], id="example 2"),
        pytest.param([], 1, 1, [], id="empty list"),
        pytest.param([1, 2], 1, 2, [2, 1], id="two nodes"),
        pytest.param([1, 2, 3, 4, 5], 1, 3, [3, 2, 1, 4, 5], id="left=1"),
    ],
)
def test_solution(fut, head, left, right, expected):
    head = ListNode.from_iterable(head)
    head = fut(head, left, right)
    actual = []
    node = head
    while node is not None:
        actual.append(node.val)
        node = node.next
    assert actual == expected
