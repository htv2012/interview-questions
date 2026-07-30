
from tree import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
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
