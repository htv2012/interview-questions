#!/usr/bin/env python3
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
from typing import Optional

from list_node import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        while current_node is not None:
            next_node = current_node
            while next_node is not None and next_node.val == current_node.val:
                next_node = next_node.next
            current_node.next = next_node
            current_node = current_node.next

        return head
