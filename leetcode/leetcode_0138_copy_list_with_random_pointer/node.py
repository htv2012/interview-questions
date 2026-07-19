import contextlib
import logging
from typing import List, Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        n = "" if self.next is None else f" n={self.next.val}"
        n = ""
        r = " r=None" if self.random is None else f" r={self.random.val}"
        return f"<Node v={self.val}{n}{r}>"


def iter_nodes(head: Optional[Node]):
    node = head
    counter = 0
    while node is not None:
        yield counter, node
        node = node.next
        counter += 1


def build(seq: Optional[List[List[int]]]) -> Node:
    li = [Node(val) for val, _ in seq or []]
    for next_index, node in enumerate(li, 1):
        with contextlib.suppress(IndexError):
            node.next = li[next_index]

    for node, (_, rand) in zip(li, seq):
        if rand is not None:
            node.random = li[rand]

    return li[0]


def to_list(head: Optional[Node]) -> List:
    indices = {}
    node = head
    for i, node in iter_nodes(head):
        indices[node] = i

    out = [
        [node.val, None if node.random is None else indices[node.random]]
        for _, node in iter_nodes(head)
    ]

    return out


def verify_lists_equal(actual: Optional[Node], expected: Optional[Node]):
    actual_list = to_list(actual)
    expected_list = to_list(expected)
    logging.debug(f"{actual_list=}")
    logging.debug(f"{expected_list=}")
    assert actual_list == expected_list


# test
head = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
li = build(head)
node = li
while node is not None:
    print(node)
    node = node.next

head2 = to_list(li)
print(head)
print(head2)
