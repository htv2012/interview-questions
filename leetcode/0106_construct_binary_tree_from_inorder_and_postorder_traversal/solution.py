from typing import List, Optional

from tree import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        root = TreeNode(val=postorder.pop())

        # Left tree
        mid = inorder.index(root.val)
        left_inorder = inorder[:mid]
        left_postorder = postorder[: len(left_inorder)]
        root.left = self.buildTree(left_inorder, left_postorder)

        # Right tree
        right_inorder = inorder[mid + 1 :]
        right_postorder = postorder[len(left_inorder) :]
        root.right = self.buildTree(right_inorder, right_postorder)

        return root
