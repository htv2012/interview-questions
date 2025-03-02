#!/usr/bin/env python3
import pytest
import tree


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param([2, 1, 3], True, id="example 1"),
        pytest.param([5, 1, 4, None, None, 3, 6], False, id="example 2"),
        pytest.param([5, 4, 6, None, None, 3, 7], False, id="wrong 1"),
    ],
)
def test_solution(fut, indata, expected):
    root = tree.breadth_first_build(indata)
    assert fut(root) is expected
