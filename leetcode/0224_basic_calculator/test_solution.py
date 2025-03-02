#!/usr/bin/env python3
import pytest


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param("1 + 1", 2, id="example 1"),
        pytest.param(" 2-1 + 2 ", 3, id="example 2"),
        pytest.param("(1+(4+5+2)-3)+(6+8)", 23, id="example 3"),
        pytest.param("(1 + 2)", 3, id="paren"),
        pytest.param("18 - 10", 8, id="simple subtraction"),
        pytest.param("1+5-4", 2, id="wrong 1"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
