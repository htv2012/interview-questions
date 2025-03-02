#!/usr/bin/env python3
import pytest
import tree


@pytest.mark.parametrize(
    "indata,expected",
    [
        pytest.param([1, None, 2, 3], [1, 3, 2], id="example 1"),
        pytest.param([], [], id="example 2"),
        pytest.param([1], [1], id="example 3"),
    ],
)
def test_solution(fut, indata, expected):
    root = tree.breadth_first_build(indata)
    assert fut(root) == expected
