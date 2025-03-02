#!/usr/bin/env python3
import pytest
import tree


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param([1, 2, 2, 3, 4, 4, 3], True, id="example 1"),
        pytest.param([1, 2, 2, None, 3, None, 3], False, id="example 2"),
        pytest.param([1, 2, 2, 2, None, 2], False, id="wrong 1"),
        pytest.param(
            [2, 3, 3, 4, 5, 5, 4, None, None, 8, 9, None, None, 9, 8],
            False,
            id="wrong 2",
        ),
        pytest.param(
            [2, 3, 3, 5, 5, 5, 5, None, None, 8, 9, None, None, 9, 8],
            False,
            id="wrong 3",
        ),
        pytest.param([1, 2, 2, 3, None, None, 3], True, id="custom 1"),
        pytest.param([1, 2, 2, 3, 4, 4, 3], True, id="custom 2"),
    ],
)
def test_solution(fut, indata, expected):
    root = tree.breadth_first_build(indata)
    assert fut(root) is expected
