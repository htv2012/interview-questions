#!/usr/bin/env python3
# https://leetcode.com/problems/reverse-linked-list/description/?envType=daily-question&envId=2024-03-13
from typing import Optional

from list_node import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node, current_node = None, head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        return prev_node
