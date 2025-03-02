"""
Definition for a n-ary tree
"""

import collections
import json
from typing import Optional


class Node:
    """N-ary Tree"""

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __repr__(self):
        children = ""
        if self.children:
            children = [node.val for node in self.children]
            children = f", {children=}"
        return f"{self.__class__.__name__}(" f"val={self.val!r}" f"{children}" f")"


def deserialize(text: str) -> Optional[Node]:
    values = json.loads(text)
    queue = collections.deque()
    pre_root = Node()
    queue.append(pre_root)

    for value in values:
        if value is None:
            node = queue.popleft()
            queue.extend(node.children or [])
        else:
            node = queue[0]
            if node.children is None:
                node.children = []
            node.children.append(Node(value))

    if pre_root.children is None:
        return None
    return pre_root.children[0]


def pad(level: int, index: int):
    if level == 0:
        return ""

    return ("    " * (level - 1)) + "|-- "


def show(root: Optional[Node], level: int = 0, index: int = 0):
    if root is None:
        return
    print(f"{pad(level, index)}{root.val}")
    for child_index, node in enumerate(root.children or []):
        show(node, level=level + 1, index=child_index)


# TODO: print
# TODO: serialize
# TODO: same tree
