#!/usr/bin/env python3
import pytest
import tree


@pytest.mark.parametrize(
    "root, start,expected",
    [
        pytest.param([1, 5, 3, None, 4, 10, 6, 9, 2], 3, 4, id="example 1"),
        pytest.param([1], 1, 0, id="example 2"),
    ],
)
def test_solution(fut, root, start, expected):
    root = tree.breadth_first_build(root)
    assert fut(root, start) == expected
