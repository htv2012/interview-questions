#!/usr/bin/env python3
import pytest


@pytest.mark.parametrize(
    "paths,expected",
    [
        pytest.param(
            [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]],
            "Sao Paulo",
            id="example 1",
        ),
        pytest.param([["B", "C"], ["D", "B"], ["C", "A"]], "A", id="example 2"),
        pytest.param([["A", "Z"]], "Z", id="example 3"),
    ],
)
def test_solution(fut, paths, expected):
    assert fut(paths) == expected
