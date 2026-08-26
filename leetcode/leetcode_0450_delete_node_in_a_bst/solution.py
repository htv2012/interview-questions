import logging
from typing import Optional

from tree import TreeNode

logger = logging.getLogger()


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        elif root.left is None and root.right is None:
            return None
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root.left
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root.right
        else:
            replacement = root.right
            while replacement.left:
                replacement = replacement.left
            replacement.left = root.left
            root = root.right
            return root
