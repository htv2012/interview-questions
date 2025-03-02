#!/usr/bin/env python3
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
from typing import List, Optional

from tree import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root_value = preorder[0]
        root = TreeNode(root_value)

        root_index = inorder.index(root_value)
        left_inorder = inorder[:root_index]
        left_node_count = len(left_inorder)
        left_preorder = preorder[1 : left_node_count + 1]
        root.left = self.buildTree(
            preorder=left_preorder,
            inorder=left_inorder,
        )

        right_inorder = inorder[root_index + 1 :]
        right_preorder = preorder[left_node_count + 1 :]
        root.right = self.buildTree(
            preorder=right_preorder,
            inorder=right_inorder,
        )

        return root
