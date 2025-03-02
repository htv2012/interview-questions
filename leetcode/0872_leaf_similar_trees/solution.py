#!/usr/bin/env python3
# https://leetcode.com/problems/leaf-similar-trees/?envType=daily-question&envId=2024-03-13
from typing import Optional

from tree import TreeNode


class Solution:
    def get_leaves(self, root: Optional[TreeNode]):
        if root is None:
            return
        yield from self.get_leaves(root.left)
        if root.left is None and root.right is None:
            yield root.val
        yield from self.get_leaves(root.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = self.get_leaves(root1)
        leaves2 = self.get_leaves(root2)
        return leaves1 == leaves2
