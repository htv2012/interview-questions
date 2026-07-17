"""
Definition for a binary tree node.
"""

import argparse
import collections
import itertools
import json
import logging
from typing import Optional


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


def same_tree(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
    que = collections.deque()
    que.append((t1, t2))

    while que:
        n1, n2 = que.popleft()
        logging.debug(f"Compare {n1} and {n2}")
        if n1 is None and n2 is None:
            continue
        elif n1 is None or n2 is None:
            return False
        elif n1.val != n2.val:
            return False
        que.append((n1.left, n2.left))
        que.append((n1.right, n2.right))

    return True

