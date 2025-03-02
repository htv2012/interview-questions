import collections
from typing import Optional


class Node:
    def __init__(self, val: int, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        return f"{self.__class__.__name__}(" f"val={self.val!r}" f")"


def breadth_first_iter(node: Node, level: int = 0):
    queue = collections.deque([(node, level)])
    while queue:
        node, level = queue.popleft()
        if node is None:
            continue
        yield node, level
        queue.append((node.left, level + 1))
        queue.append((node.right, level + 1))


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        last_level: Node = -1
        last_node: Node = None

        for node, level in breadth_first_iter(root):
            node.next = None
            if last_level == level:
                last_node.next = node
            last_level = level
            last_node = node
