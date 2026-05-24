from typing import List, Optional

from tree import TreeNode


def post_order(root: Optional[TreeNode]) -> List[int]:
    out = []
    stack = [(root, False)]  # [(node, ready)]

    while stack:
        node, ready = stack.pop()
        if node is None:
            continue

        if ready:
            out.append(node.val)
        else:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))

    return out


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return post_order(root)
