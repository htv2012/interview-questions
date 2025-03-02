#!/usr/bin/env python3
import pytest


@pytest.mark.parametrize(
    "preorder, inorder, expected",
    [
        pytest.param(
            [3, 9, 20, 15, 7],
            [9, 3, 15, 20, 7],
            [3, 9, 20, None, None, 15, 7],
            id="example 1",
        ),
        pytest.param(
            [-1],
            [-1],
            [-1],
            id="example 1",
        ),
    ],
)
def test_solution(fut, preorder, inorder, expected):
    pass
