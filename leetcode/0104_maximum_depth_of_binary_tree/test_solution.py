#!/usr/bin/env python3
import pytest
from tree import breadth_first_build


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param([3, 9, 20, None, None, 15, 7], 3, id="example 1"),
        pytest.param([1, None, 2], 2, id="example 2"),
        pytest.param(range(15), 4, id="custom1"),
        pytest.param(range(16), 5, id="custom2"),
    ],
)
def test_solution(fut, indata, expected):
    root = breadth_first_build(indata)
    assert fut(root) == expected
