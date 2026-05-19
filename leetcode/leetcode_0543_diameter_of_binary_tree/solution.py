#!/usr/bin/env python3
"""
https://leetcode.com/problems/diameter-of-binary-tree/?envType=daily-question&envId=2024-03-13
"""

import itertools
import logging
from typing import Optional

logger = logging.getLogger()


class TreeNode:
    """Binary Tree"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"N({self.val})"


def make_node(value):
    if value is None:
        return None
    return TreeNode(value)


def breadth_first_build(seq):
    if not seq:
        return None

    sides = itertools.cycle(["left", "right"])
    seq = iter(seq)
    root = make_node(next(seq))
    que = [root]

    for side, value in zip(sides, seq):
        node = make_node(value)
        setattr(que[0], side, node)
        if node:
            que.append(node)
        if side == "right":
            que.pop(0)

    return root


def diameter(t: TreeNode) -> int:
    if t is None:
        res = -1
    elif t.left is None and t.right is None:
        res = 0
    else:
        res = 2 + diameter(t.left) + diameter(t.right)
    logger.debug(f"dia({t}) -> {res}")
    return res


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return diameter(root)
