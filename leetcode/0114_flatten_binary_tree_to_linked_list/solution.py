#!/usr/bin/env python3
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
from typing import Optional

from tree import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return None

        left_tree, right_tree = root.left, root.right
        self.flatten(left_tree)
        self.flatten(right_tree)

        root.left = None
        root.right = left_tree

        node = root
        while node.right is not None:
            node = node.right
        node.right = right_tree
