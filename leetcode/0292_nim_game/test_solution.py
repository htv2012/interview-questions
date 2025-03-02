#!/usr/bin/env python3
import pytest


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param(1, True, id="example 1"),
        pytest.param(2, True, id="example 2"),
        pytest.param(3, True, id="3"),
        pytest.param(4, False, id="4"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
