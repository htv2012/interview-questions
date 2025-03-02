#!/usr/bin/env python3
# https://leetcode.com/problems/reverse-linked-list-ii/description/
from typing import Optional

from list_node import ListNode


def get_node_at_position(head: Optional[ListNode], position: int) -> Optional[ListNode]:
    if position == 0:
        return ListNode(0, next=head)

    for _ in range(1, position):
        head = head.next
    return head


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        """
        left = 2, right = 4
        head -> 1 -> 2 -> 3 -> 4 -> 5
                |    |         |    |
                |    lelf      right|
                |                   |
                tail                bound
        """
        if head is None or head.next is None:
            return head

        tail = get_node_at_position(head, left - 1)
        previous_node = bound = get_node_at_position(tail, right - left + 3)
        current_node = tail.next

        while current_node is not bound:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        tail.next = previous_node
        if left == 1:
            head = tail.next
        return head
