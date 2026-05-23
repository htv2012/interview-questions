#!/usr/bin/env python3
"""
https://leetcode.com/problems/diameter-of-binary-tree/?envType=daily-question&envId=2024-03-13
"""

import enum
import itertools
import logging
from typing import Optional

logger = logging.getLogger()


class VisitState(enum.Enum):
    VISITED = enum.auto()
    NOT_VISITED = enum.auto()


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


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    diameter = 0
    height = {None: 0}  # node: height
    stack = [(root, VisitState.NOT_VISITED)]  # [(node, visited_state)]

    while stack:
        node, visited = stack.pop()
        if node is None:
            continue
        if visited == VisitState.NOT_VISITED:
            stack.append((node, VisitState.VISITED))
            stack.append((node.left, VisitState.NOT_VISITED))
            stack.append((node.right, VisitState.NOT_VISITED))
        else:
            left_height = height[node.left]
            right_height = height[node.right]
            height[node] = 1 + max(left_height, right_height)
            diameter = max(diameter, left_height + right_height)

    return diameter


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return diameter_of_binary_tree(root)
