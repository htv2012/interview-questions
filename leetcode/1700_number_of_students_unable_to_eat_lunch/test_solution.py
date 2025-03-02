#!/usr/bin/env python3
import pytest


@pytest.mark.parametrize(
    "students, sandwiches, expected",
    [
        pytest.param([1, 1, 0, 0], [0, 1, 0, 1], 0, id="example 1"),
        pytest.param([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1], 3, id="example 2"),
    ],
)
def test_solution(fut, students, sandwiches, expected):
    assert fut(students, sandwiches) == expected
