#!/usr/bin/env python3
# https://leetcode.com/problems/palindrome-linked-list/description/?envType=daily-question&envId=2024-03-13
from typing import Optional

from list_node import ListNode


class Solution:
    def values(self, head: Optional[ListNode]):
        node = head
        while node is not None:
            yield node.val
            node = node.next

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        # Count number of nodes
        count, node = 0, head
        while node:
            count += 1
            node = node.next

        # Locate the tail
        tail = head
        for _ in range((count + 1) // 2):
            tail = tail.next
        tail_values = reversed(list(self.values(tail)))

        node = head
        for tail_value in tail_values:
            if node.val != tail_value:
                return False
            node = node.next
        return True
