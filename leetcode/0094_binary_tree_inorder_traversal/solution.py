# https://leetcode.com/problems/binary-tree-inorder-traversal/?envType=daily-question&envId=2024-03-13

from tree import TreeNode


class Solution:
    def inorder(self, root: TreeNode | None, out: list):
        if root is None:
            return
        self.inorder(root.left, out)
        out.append(root.val)
        self.inorder(root.right, out)

    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        out = []
        self.inorder(root, out)
        return out
