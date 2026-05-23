#!/usr/bin/env python3
"""
https://leetcode.com/problems/diameter-of-binary-tree/?envType=daily-question&envId=2024-03-13
"""

import enum
from typing import Optional

from tree import TreeNode


class CalculationState(enum.Enum):
    READY = enum.auto()
    NOT_READY = enum.auto()


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    diameter = 0
    height = {None: 0}  # node: height
    stack = [(root, CalculationState.NOT_READY)]

    while stack:
        node, calculation_state = stack.pop()
        if node is None:
            continue

        if calculation_state == CalculationState.READY:
            left_height = height[node.left]
            right_height = height[node.right]
            height[node] = 1 + max(left_height, right_height)
            diameter = max(diameter, left_height + right_height)
        else:
            stack.append((node, CalculationState.READY))
            stack.append((node.left, CalculationState.NOT_READY))
            stack.append((node.right, CalculationState.NOT_READY))

    return diameter


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return diameter_of_binary_tree(root)
