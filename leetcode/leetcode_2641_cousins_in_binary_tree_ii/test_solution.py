"""
https://leetcode.com/problems/cousins-in-binary-tree-ii/
"""

import collections
import logging
from typing import Optional

import pytest
from tree import TreeNode, breadth_first_build

from solution import Solution

logger = logging.getLogger()


@pytest.fixture
def fut():
    sol = Solution()
    return sol.replaceValueInTree


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["root"],
        kwargs["expected"],
        id=test_id,
    )


def same_tree(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
    que = collections.deque()
    que.append_left((t1, t2))

    while que:
        node1, node2 = que.pop()
        if node1 is None and node2 is None:
            continue
        elif node1 is None or node2 is None:
            logger.debug(
                f"Trees differ because of the node is None: {node1=}, {node2=}"
            )
            return False

        if node1.val != node2.val:
            logger.debug(
                f"Trees differ because values are different: {node1=}, {node2=}"
            )
            return False

        que.append((node1.left, node2.left))
        que.append((node1.right, node2.right))

    return True


@pytest.mark.parametrize(
    "root, expected",
    [
        tc(
            test_id="Example 1",
            root=[5, 4, 9, 1, 10, None, 7],
            expected=[0, 0, 0, 7, 7, None, 11],
        ),
        tc(
            test_id="Example 2",
            root=[3, 1, 2],
            expected=[0, 0, 0],
        ),
    ],
)
def test_solution(fut, root, expected):
    root = breadth_first_build(root)
    root = fut(root)
    expected = breadth_first_build(expected)
    assert same_tree(root, expected)
