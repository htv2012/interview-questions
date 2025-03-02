#!/usr/bin/env python3
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
from typing import Optional

from list_node import ListNode
from tree import TreeNode


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Shortcuts, could be optimized later
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)

        # Count number of nodes
        count = 0
        node = head
        while node is not None:
            count += 1
            node = node.next

        # Break list into 3 parts: list1, middle node, list2
        pre, mid = None, head
        for _ in range(count // 2):
            pre, mid = mid, mid.next

        # Build left tree from the first list
        pre.next = None
        left_tree = self.sortedListToBST(head)
        pre.next = mid

        # Build right tree from the second list
        right_tree = self.sortedListToBST(mid.next)

        # Build the root with the middle node
        return TreeNode(mid.val, left=left_tree, right=right_tree)


def build(head: Optional[ListNode]) -> Optional[TreeNode]:
    return Solution().sortedListToBST(head)
