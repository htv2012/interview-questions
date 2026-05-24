"""
https://leetcode.com/problems/binary-tree-postorder-traversal/description/
"""

import pytest

from solution import post_order
from tree import breadth_first_build


@pytest.mark.parametrize(
    ["seq", "expected"],
    [
        pytest.param([1, None, 2, 3], [3, 2, 1], id="Example 1"),
        pytest.param(
            [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9],
            [4, 6, 7, 5, 2, 9, 8, 3, 1],
            id="Example 2",
        ),
        pytest.param([], [], id="Example 3"),
        pytest.param([1], [1], id="Example 4"),
    ],
)
def test_solution(seq, expected):
    root = breadth_first_build(seq)
    assert post_order(root) == expected
