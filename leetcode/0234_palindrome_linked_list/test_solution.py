#!/usr/bin/env python3
import pytest
from list_node import ListNode


@pytest.mark.parametrize(
    "indata,expected",
    [
        pytest.param([1, 2, 2, 1], True, id="example 1"),
        pytest.param([1, 2], False, id="example 2"),
        pytest.param([], True, id="empty list"),
        pytest.param([1], True, id="single node"),
        pytest.param([1, 2, 3, 1], False, id="even elements, expect false"),
        pytest.param([1, 2, 3, 4, 3, 2, 1], True, id="odd elements, expect true"),
        pytest.param([1, 2, 3, 4, 5, 2, 1], False, id="odd elements, expect false"),
    ],
)
def test_solution(fut, indata, expected):
    head = ListNode.from_iterable(indata)
    assert fut(head) is expected
