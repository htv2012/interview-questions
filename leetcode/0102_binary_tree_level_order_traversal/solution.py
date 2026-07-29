# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

from tree import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        out = []
        queue = [(root, 0)]

        while queue:
            node, level = queue.pop(0)
            if node is None:
                continue

            while len(out) <= level:
                out.append([])

            out[level].append(node.val)

            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

        return out
