"""
Definition for a binary tree node.
"""

import argparse
import collections
import itertools
import json
from typing import Optional

from drawtree.drawtree import drawtree


class TreeNode:
    """Binary Tree"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"N({self.val})"

    def insert(self, node):
        if node.val < self.val:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)
        elif node.val > self.val:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)
        else:  # node.val == self.val:
            raise ValueError(f"Duplicate: {node.val}")

    @classmethod
    def from_iterable(cls, it):
        it = next(it)
        root = cls(next(it))
        for value in it:
            root.insert(cls(value))
        return root


def breadth_first_build(seq):
    def _build(value):
        if value is None:
            return None
        return TreeNode(value)

    if not seq:
        return None

    if not seq:
        return None

    sides = itertools.cycle(["left", "right"])
    seq = iter(seq)
    root = _build(next(seq))
    que = [root]

    for side, value in zip(sides, seq):
        node = _build(value)
        setattr(que[0], side, node)
        if node:
            que.append(node)
        if side == "right":
            que.pop(0)

    return root


def deserialize(text: str) -> Optional[TreeNode]:
    seq = json.loads(text)
    return breadth_first_build(seq)


def serialize(root: Optional[TreeNode]) -> str:
    queue = collections.deque()
    if root is not None:
        queue.append(root)

    out = []
    while queue:
        node = queue.popleft()
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

    # Remove trailing nulls
    while out[-1] is None:
        out.pop()
    return json.dumps(out, separators=(",", ":"))


def pre_order_iter(root: Optional[TreeNode]):
    if root is None:
        return
    yield root
    yield from pre_order_iter(root.left)
    yield from pre_order_iter(root.right)


def breadth_first_iter(node: TreeNode, level: int = 0):
    queue = collections.deque([(node, level)])
    while queue:
        node, level = queue.popleft()
        if node is None:
            continue
        yield node, level
        queue.append((node.left, level + 1))
        queue.append((node.right, level + 1))


def inorder_iter(node: Optional[TreeNode]):
    if node is None:
        return
    yield from inorder_iter(node.left)
    yield node
    yield from inorder_iter(node.right)


def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    left_depth = max_depth(root.left) + 1
    right_depth = max_depth(root.right) + 1
    return max(left_depth, right_depth)


def main():
    """Draw tree via deserialize."""
    parser = argparse.ArgumentParser()
    parser.add_argument("json_text")
    args = parser.parse_args()
    print(args)

    root = deserialize(args.json_text)
    drawtree(root)


if __name__ == "__main__":
    main()
