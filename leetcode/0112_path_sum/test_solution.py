#!/usr/bin/env python3
import pytest
import tree


@pytest.mark.parametrize(
    "root, target_sum, expected",
    [
        pytest.param(
            [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],
            22,
            True,
            id="example 1",
        ),
        pytest.param([1, 2, 3], 5, False, id="example 2"),
    ],
)
def test_solution(fut, root, target_sum, expected):
    root = tree.breadth_first_build(root)
    assert fut(root, target_sum) is expected
