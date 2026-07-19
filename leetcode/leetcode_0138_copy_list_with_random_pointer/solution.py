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

        li = [Node(val) for val, _ in in_list]
        li.append(None)  # Last element: The null node

        for i in range(len(li) - 1):
            li[i].next = li[i + 1]

        for (_, random_index), node in zip(in_list, li):
            node.random = li[random_index]

        return li[0]
