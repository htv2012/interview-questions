from queue import SimpleQueue

from tree import TreeNode


class Solution:
    def addOneRow(self, root: TreeNode | None, val: int, depth: int) -> TreeNode | None:
        if depth == 1:
            return TreeNode(val=val, left=root)

        queue = SimpleQueue()
        queue.put((root, 1))

        while not queue.empty():
            node, node_depth = queue.get()
            if node is None:
                continue

            if node_depth + 1 == depth:
                node.left = TreeNode(val=val, left=node.left)
                node.right = TreeNode(val=val, right=node.right)
            else:
                queue.put((node.left, node_depth + 1))
                queue.put((node.right, node_depth + 1))

        return root
