#!/usr/bin/env python3
import pytest


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param([1, 2, 3], [1, 2, 4], id="example 1"),
        pytest.param([4, 3, 2, 1], [4, 3, 2, 2], id="example 2"),
        pytest.param([9], [1, 0], id="example 3"),
        pytest.param([9, 9], [1, 0, 0], id="99"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
