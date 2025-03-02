#!/usr/bin/env python3
import pytest


@pytest.mark.parametrize(
    "equations, values, queries, expected",
    [
        pytest.param(
            [["a", "b"], ["b", "c"]],
            [2.0, 3.0],
            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
            [6.00000, 0.50000, -1.00000, 1.00000, -1.00000],
            id="example 1",
        ),
        pytest.param(
            [["a", "b"], ["b", "c"], ["bc", "cd"]],
            [1.5, 2.5, 5.0],
            [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
            [3.75000, 0.40000, 5.00000, 0.20000],
            id="example 2",
        ),
        pytest.param(
            [["a", "b"]],
            [0.5],
            [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]],
            [0.50000, 2.00000, -1.00000, -1.00000],
            id="example 3",
        ),
        pytest.param(
            [["a", "e"], ["b", "e"]],
            [4.0, 3.0],
            [["a", "b"], ["e", "e"], ["x", "x"]],
            [1.33333, 1.00000, -1.00000],
            id="wrong 1",
        ),
        pytest.param(
            [["a", "b"], ["b", "c"]],
            [2.0, 3.0],
            [["a", "e"]],
            [-1.00000],
            id="example 1-debug",
        ),
    ],
)
def test_solution(fut, equations, values, queries, expected):
    actual = fut(equations, values, queries)
    assert actual == pytest.approx(expected, abs=0.01)
    # assert actual == expected
