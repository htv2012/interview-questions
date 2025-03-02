#!/usr/bin/env python3
import pytest
import tree


@pytest.mark.parametrize(
    "root, target_sum, expected",
    [
        pytest.param(
            [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1],
            22,
            [[5, 4, 11, 2], [5, 8, 4, 5]],
            id="example 1",
        ),
        pytest.param([1, 2, 3], 5, [], id="example 2"),
    ],
)
def test_solution(fut, root, target_sum, expected):
    root = tree.breadth_first_build(root)
    for path in fut(root, target_sum):
        expected.remove(path)
    assert expected == []
