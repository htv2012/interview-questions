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


def divide(count: int, parts) -> list:
    """
    Divide count into parts.

    >>> divide(35, 7)
    [5, 5, 5, 5, 5, 5, 5]

    >>> divide(37, 7)
    [6, 6, 5, 5, 5, 5, 5]

    >>> divide(25, 4)
    [7, 6, 6, 6]

    >>> divide(3, 1)
    [3]

    >>> divide(3, 7)
    [1, 1, 1, 0, 0, 0, 0]
    """
    quotient, remainder = divmod(count, parts)
    return [quotient + 1 if i < remainder else quotient for i in range(parts)]


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        if k == 1:
            return [head]

        out = [None] * k
        nodes_count = count_nodes(head)
        if nodes_count == 0:
            return out

        node = head
        for seg, count in zip(range(k), divide(nodes_count, k)):
            out[seg] = node
            prev = None
            for _ in range(count):
                prev = node
                if node is None:
                    break
                node = node.next

            prev.next = None

        return out
