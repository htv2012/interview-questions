#!/usr/bin/env python3
import pytest
import tree


@pytest.mark.parametrize(
    "root1, root2, expected",
    [
        pytest.param(
            [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4],
            [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8],
            True,
            id="example 1",
        ),
        pytest.param(
            [1, 2, 3],
            [1, 3, 2],
            False,
            id="example 2",
        ),
    ],
)
def test_solution(fut, root1, root2, expected):
    root1 = tree.breadth_first_build(root1)
    root2 = tree.breadth_first_build(root2)
    assert fut(root1, root2) is expected
