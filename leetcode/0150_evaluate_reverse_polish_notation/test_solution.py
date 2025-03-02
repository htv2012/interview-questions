#!/usr/bin/env python3
import pytest


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param(["2", "1", "+", "3", "*"], 9, id="example 1"),
        pytest.param(["4", "13", "5", "/", "+"], 6, id="example 2"),
        pytest.param(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
            22,
            id="example 3",
        ),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
