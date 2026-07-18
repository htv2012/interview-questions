from typing import Optional

from node import Node


def iter_nodes(head: Optional[Node]):
    node = head
    counter = 0
    while node is not None:
        yield counter, node
        node = node.next
        counter += 1


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        node_list = [Node(node.val) for _, node in iter_nodes(head)]

