#!/usr/bin/env python3
import pytest

from solution import NestedInteger, NestedIterator


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param([[1, 1], 2, [1, 1]], [1, 1, 2, 1, 1], id="example 1"),
        pytest.param([1, [4, [6]]], [1, 4, 6], id="example 2"),
        pytest.param([[[1]]], [1], id="deep"),
        pytest.param([[], []], [], id="empty"),
        pytest.param([[[]]], [], id="nested empty"),
    ],
)
def test_solution(indata, expected):
    nested_list = [NestedInteger(v) for v in indata]
    nested_iterator = NestedIterator(nested_list)
    actual = []
    while nested_iterator.hasNext():
        actual.append(nested_iterator.next())
    assert actual == expected
