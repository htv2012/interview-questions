#!/usr/bin/env python3
import pytest
import tree


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param([1, 2, 5, 3, 4, None, 6], [1, 2, 3, 4, 5, 6], id="example 1"),
        pytest.param([], [], id="example 2"),
        pytest.param([0], [0], id="example 3"),
        pytest.param([1, 2, 3], [1, 2, 3], id="custom 1"),
    ],
)
def test_solution(fut, indata, expected):
    root = tree.breadth_first_build(indata)
    fut(root)

    node = root
    for value in expected:
        assert node.val == value
        assert node.left is None
        node = node.right

    assert node is None
