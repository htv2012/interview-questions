"""
Definition for a binary tree node.
"""

import itertools

from graphviz import Digraph


class TreeNode:
    """Binary Tree"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"N({self.val})"


def breadth_first_build(seq):
    def _build(value):
        if value is None:
            return None
        return TreeNode(value)

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


def draw_tree(root):
    if not root:
        return "Empty Tree"

    dot = Digraph()
    # Use circle shape for a clean look
    dot.attr("node", shape="circle")

    def add_nodes_edges(node):
        # Create a unique ID for the node using its memory address
        node_id = str(id(node))
        dot.node(node_id, label=str(node.val))

        if node.left:
            left_id = str(id(node.left))
            dot.edge(node_id, left_id)
            add_nodes_edges(node.left)

        if node.right:
            right_id = str(id(node.right))
            dot.edge(node_id, right_id)
            add_nodes_edges(node.right)

    add_nodes_edges(root)
    return dot
