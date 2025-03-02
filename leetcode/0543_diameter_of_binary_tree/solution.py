#!/usr/bin/env python3
# https://leetcode.com/problems/diameter-of-binary-tree/?envType=daily-question&envId=2024-03-13
from typing import Optional

from tree import TreeNode


def height(node: TreeNode):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1

    left_height = height(node.left)
    right_height = height(node.right)
    return 1 + max(left_height, right_height)


def diameter(node: TreeNode, level=0, maxsofar: int = 0) -> int:
    if node is None:
        return max(maxsofar, 0)
    elif node.left is None and node.right is None:
        return max(maxsofar, 0)
    elif node.left is None:
        return max(maxsofar, diameter(node.right) + 1)
    elif node.right is None:
        return max(maxsofar, diameter(node.left) + 1)
    else:
        out = height(node.left) + height(node.right)
        return max(maxsofar, out)


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return diameter(root)
