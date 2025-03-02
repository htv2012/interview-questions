from typing import Optional

from list_node import ListNode


def iter_nodes(head: ListNode):
    while head is not None:
        next_node = head.next
        head.next = None
        yield head
        head = next_node


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lt = lt_tail = ListNode()  # Nodes with values less than x
        ge = ge_tail = ListNode()  # Nodes with values greater than or equal to x

        for node in iter_nodes(head):
            if node.val < x:
                lt_tail.next = node
                lt_tail = lt_tail.next
            else:
                ge_tail.next = node
                ge_tail = ge_tail.next

        lt_tail.next = ge.next
        return lt.next
