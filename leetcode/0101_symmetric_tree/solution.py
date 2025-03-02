#!/usr/bin/env python3
# https://leetcode.com/problems/symmetric-tree/description/
from typing import Optional

from tree import TreeNode


def mirror_compare(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False
    if root1.val != root2.val:
        return False
    return mirror_compare(root1.left, root2.right) and mirror_compare(
        root1.right, root2.left
    )


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return mirror_compare(root.left, root.right)
