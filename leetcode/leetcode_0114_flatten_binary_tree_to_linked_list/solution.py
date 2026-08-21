# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/

from tree import TreeNode


class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        if root is None:
            return

        left_tree, right_tree = root.left, root.right
        self.flatten(left_tree)
        self.flatten(right_tree)

        root.left = None
        root.right = left_tree

        node = root
        while node.right is not None:
            node = node.right
        node.right = right_tree
