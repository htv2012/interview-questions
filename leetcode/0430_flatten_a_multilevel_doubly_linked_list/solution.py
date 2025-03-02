from typing import Optional

from support import Node


def iter_nodes(node: Optional[Node]):
    while node:
        yield node
        yield from iter_nodes(node.child)
        node = node.next


class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        dummy = dup = Node(None, None, None, None)
        for node in iter_nodes(head):
            dup.next = Node(val=node.val, prev=dup, next=None, child=None)
            dup = dup.next
        if dummy is not dup:
            dummy.next.prev = None
        return dummy.next
