#!/usr/bin/env python3
import pytest
from tree import TreeNode, breadth_first_build


@pytest.mark.parametrize(
    "root, expected",
    [
        pytest.param([1, 2, 3, 4, 5], 3, id="example 1"),
        pytest.param([1, 2], 1, id="example 2"),
        pytest.param([1], 0, id="single node"),
        # pytest.param([0, 1, None, ], 0, id="single node"),
        pytest.param([4, 2, None, 1, 3], 2, id="incorrect 1"),
    ],
)
def test_solution(fut, root, expected):
    root = breadth_first_build(root)
    assert fut(root) == expected


def test_none(fut):
    assert fut(None) == 0


def test_no_left_tree(fut):
    root = TreeNode(0, right=TreeNode(1))
    assert fut(root) == 1

    root.right.right = TreeNode(2)
    assert fut(root) == 2

    root.right.right.right = TreeNode(3)
    assert fut(root) == 3
