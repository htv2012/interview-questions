#!/usr/bin/env python3
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
from typing import List, Optional

from tree import TreeNode


def from_pre(preorder, from_index, to_index):
    if from_index >= to_index:
        return None

    root = TreeNode(preorder[from_index])

    boundary = from_index + 1
    while boundary < to_index and preorder[boundary] < root.val:
        boundary += 1

    root.left = from_pre(
        preorder=preorder, from_index=from_index + 1, to_index=boundary
    )
    root.right = from_pre(
        preorder=preorder,
        from_index=boundary,
        to_index=to_index,
    )
    return root


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return from_pre(
            preorder=preorder,
            from_index=0,
            to_index=len(preorder),
        )
