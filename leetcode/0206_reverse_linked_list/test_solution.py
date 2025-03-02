#!/usr/bin/env python3
import pytest
from list_node import ListNode, iter_list


@pytest.mark.parametrize(
    "indata,expected",
    [
        pytest.param([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], id="example 1"),
        pytest.param([1, 2], [2, 1], id="example 2"),
        pytest.param([], [], id="example 3"),
        pytest.param([1], [1], id="one node"),
        pytest.param([1, 2], [2, 1], id="two nodes"),
        pytest.param([1, 2, 3], [3, 2, 1], id="three nodes"),
    ],
)
def test_solution(fut, indata, expected):
    head = ListNode.from_iterable(indata)
    head = fut(head)
    actual = [node.val for node in iter_list(head)]
    assert actual == expected
