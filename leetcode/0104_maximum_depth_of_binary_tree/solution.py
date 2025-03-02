#!/usr/bin/env python3
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
from typing import Optional

from tree import TreeNode


def max_depth(root: Optional[TreeNode], depth=0):
    if root is None:
        return depth
    left_depth = max_depth(root.left, depth=depth + 1)
    right_depth = max_depth(root.right, depth=depth + 1)
    return max(left_depth, right_depth)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return max_depth(root)
