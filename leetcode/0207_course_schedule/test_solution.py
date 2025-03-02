#!/usr/bin/env python3
import pytest


@pytest.mark.parametrize(
    "num_courses, prerequisites, expected",
    [
        pytest.param(2, [[1, 0]], True, id="example 1"),
        pytest.param(2, [[1, 0], [0, 1]], False, id="example 2"),
    ],
)
def test_solution(fut, num_courses, prerequisites, expected):
    assert fut(num_courses, prerequisites) is expected
