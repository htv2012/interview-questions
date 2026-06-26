"""
https://leetcode.com/problems/create-binary-tree-from-descriptions/
"""

import logging
from typing import Optional

import pytest
from tree import TreeNode, breadth_first_build

from solution import Solution

logger = logging.getLogger()


@pytest.fixture
def fut():
    sol = Solution()
    return sol.createBinaryTree


def is_same_tree(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
    que = [(t1, t2)]
    while que:
        node1, node2 = que.pop(0)
        if (node1 is None and node2 is not None) or (
            node1 is not None and node2 is None
        ):
            logging.debug(f"One of the nodes is None: {node1}, {node2}")
            return False
        elif node1 is None and node2 is None:
            continue

        # At this point, nether node1 nor node2 are None
        if node1.val != node2.val:
            logging.debug("Values differ: {node1}, {node2}")
            return False

        que.append((node1.left, node2.left))
        que.append((node1.right, node2.right))

    # We exhausted the nodes. Trees must be the same
    return True


@pytest.mark.parametrize(
    "descriptions,expected",
    [
        (
            [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]],
            [50, 20, 80, 15, 17, 19],
        ),
        ([[1, 2, 1], [2, 3, 0], [3, 4, 1]], [1, 2, None, None, 3, 4]),
        ([], []),
        ([[1, 2, 1]], [1, 2]),
    ],
    ids=["example1", "example2", "empty", "simple tree"],
)
def test_solution(fut, descriptions, expected):
    actual_root = fut(descriptions)
    expected_root = breadth_first_build(expected)
    assert is_same_tree(actual_root, expected_root)
