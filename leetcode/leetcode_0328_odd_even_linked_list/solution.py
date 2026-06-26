from typing import Optional

from list_node import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def append_node(head, tail, node):
    if tail is not None:
        tail.next = node

    return head or node, node


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_head = None
        even_tail = None
        odd_node = head

        while odd_node is not None:
            even_node = odd_node.next
            if even_node is None:
                break

            odd_node.next = even_node.next
            even_node.next = None
            even_head, even_tail = append_node(even_head, even_tail, even_node)

            if odd_node.next is None:
                break

            odd_node = odd_node.next

        if odd_node is not None:
            odd_node.next = even_head
        return head
