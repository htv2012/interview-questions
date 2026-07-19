from typing import Optional

from node import Node


def iter_nodes(head: "Optional[Node]"):
    node = head
    counter = 0
    while node is not None:
        yield counter, node
        node = node.next
        counter += 1


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        index = {node: i for i, node in iter_nodes(head)}
        index[None] = len(index)
        in_list = [[node.val, index[node.random]] for _, node in iter_nodes(head)]

        out_list = [Node(val) for val, _ in in_list]
        out_list.append(None)

        for i in range(len(out_list) - 1):
            out_list[i].next = out_list[i + 1]

        for (_, irand), node in zip(in_list, out_list):
            node.random = out_list[irand]

        return out_list[0]
