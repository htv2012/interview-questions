#!/usr/bin/env python3
# https://leetcode.com/problems/validate-binary-search-tree/
from typing import Optional

from tree import TreeNode


def inorder(root, visit):
    if root is None:
        return
    inorder(root.left, visit)
    visit(root)
    inorder(root.right, visit)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        seq = []

        def visit(node):
            nonlocal seq
            seq.append(node.val)

        inorder(root, visit)
        prev = seq[0] - 1
        for value in seq:
            if prev >= value:
                return False
            prev = value
        return True
