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


def partition(n: int, k: int):
    """Partition n elements into k groups.

    Yield the indices where the head of a list should be.
    """
    group_size, remainder = divmod(n, k)
    index = 0
    for i in range(k):
        index += group_size + 1 if i < remainder else group_size
        yield index


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        nodes_count = count_nodes(head)
        head_indices = partition(nodes_count, k)
        head_index = next(head_indices)
        heads = [head]
        previous_node, current_node = None, head

        for i in range(nodes_count):
            if i == head_index:
                previous_node.next = None
                heads.append(current_node)
                head_index = next(head_indices)
            previous_node, current_node = current_node, current_node.next

        while len(heads) < k:
            heads.append(None)

        return heads
