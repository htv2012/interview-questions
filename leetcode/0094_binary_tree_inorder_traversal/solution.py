#!/usr/bin/env python3
# https://leetcode.com/problems/binary-tree-inorder-traversal/?envType=daily-question&envId=2024-03-13
from typing import List, Optional

from tree import TreeNode


class Solution:
    def inorder(self, root: Optional[TreeNode], out: List):
        if root is None:
            return
        self.inorder(root.left, out)
        out.append(root.val)
        self.inorder(root.right, out)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        self.inorder(root, out)
        return out
