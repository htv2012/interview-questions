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


def partition(n: int, k: int):
    """Partition n elements into k groups."""
    quo, rem = divmod(n, k)
    acc = 0
    for i in range(k):
        acc += quo + 1 if i < rem else quo
        yield acc


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        if k == 1:
            return [head]

        nodes_count = count_nodes(head)
        if nodes_count == 0:
            return [None] * k

        prev, node = None, head
        partitions = partition(nodes_count, k)
        head_index = next(partitions)
        out = [head]
        for i in range(nodes_count):
            if i == head_index:
                prev.next = None
                out.append(node)
                head_index = next(partitions)
            prev, node = node, node.next

        while len(out) < k:
            out.append(None)
