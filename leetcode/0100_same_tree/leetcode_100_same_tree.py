#!/usr/bin/env python3
from typing import Optional

from tree import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        try:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(
                    p.right, q.right
                )
        except AttributeError:
            pass
        return False
