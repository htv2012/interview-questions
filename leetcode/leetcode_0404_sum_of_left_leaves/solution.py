import collections

from tree import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        out = 0
        queue = collections.deque([(root, None)])

        while queue:
            node, side = queue.popleft()
            if node is None:
                continue
            if node.left is None and node.right is None and side == "left":
                out += node.val
            queue.append((node.left, "left"))
            queue.append((node.right, "right"))

        return out
