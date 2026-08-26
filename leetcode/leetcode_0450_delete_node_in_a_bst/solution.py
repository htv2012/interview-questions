from typing import Optional

from tree import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        # Gets here means root.val == key, root is the node we want to delete
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            # Find the successor: the left most node of the right sub-tree
            successor = root.right
            while successor.left is not None:
                successor = successor.left

            successor.left = root.left
            return root.right
