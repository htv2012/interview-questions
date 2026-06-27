from typing import List, Optional

from list_node import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def count_nodes(head: Optional[ListNode]) -> int:
    nodes_count = 0
    node = head
    while node is not None:
        nodes_count += 1
        node = node.next
    return nodes_count


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        out = [None] * k
        nodes_count = count_nodes(head)
        if k == 1:
            return [head]
        if nodes_count == 0:
            return out

        return [nodes_count]
