import collections
import json
from typing import Optional

from tree import TreeNode


def breadth_first_iter(node: TreeNode, level: int = 0):
    queue = collections.deque([(node, level)])
    while queue:
        node, level = queue.popleft()
        if node is None:
            continue
        yield node, level
        queue.append((node.left, level + 1))
        queue.append((node.right, level + 1))


def breadth_first_bst_build(seq):
    def _build(value):
        if value is None:
            return None
        return TreeNode(value)

    def _insert(node: TreeNode, value: int):
        if value < node.val:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                _insert(node.left, value)
        elif value > node.val:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                _insert(node.right, value)

    if not seq:
        return None

    seq = iter(seq)
    root = TreeNode(next(seq))
    for value in seq:
        _insert(root, value)
    return root


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        values = [node.val for node, _ in breadth_first_iter(root)]
        out = json.dumps(values)
        return out

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        values = json.loads(data)
        root = breadth_first_bst_build(values)
        return root
