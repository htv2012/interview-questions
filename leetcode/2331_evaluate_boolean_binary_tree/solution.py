from typing import Optional

from tree import TreeNode


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 0:
            return False
        elif root.val == 1:
            return True
        elif root.val == 2:
            left = self.evaluateTree(root.left) if root.left else False
            right = self.evaluateTree(root.right) if root.right else False
            return left or right
        elif root.val == 3:
            left = self.evaluateTree(root.left) if root.left else True
            right = self.evaluateTree(root.right) if root.right else True
            return left and right
