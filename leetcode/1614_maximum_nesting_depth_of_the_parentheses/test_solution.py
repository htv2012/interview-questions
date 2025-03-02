#!/usr/bin/env python3
import pytest


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param("(1+(2*3)+((8)/4))+1", 3, id="example 1"),
        pytest.param("(1)+((2))+(((3)))", 3, id="example 2"),
        pytest.param("", 0, id="empty string"),
        pytest.param("123", 0, id="no parens"),
        pytest.param("()", 1, id="single pair"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
