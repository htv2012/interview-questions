from typing import Optional

from tree import TreeNode


def dfs(node: Optional[TreeNode], path: tuple = None):
    if node is None:
        return

    path = path or tuple()
    yield from dfs(node.left, path + ("L",))
    yield node, list(path)
    yield from dfs(node.right, path + ("R",))


class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        start_path = dest_path = None

        for node, path in dfs(root):
            if start_path is not None and dest_path is not None:
                break
            if node.val == startValue:
                start_path = path
            elif node.val == destValue:
                dest_path = path

        # Remove steps up to LCA
        while start_path and dest_path and start_path[0] == dest_path[0]:
            start_path.pop(0)
            dest_path.pop(0)

        start_path = ["U"] * len(start_path)
        return "".join(start_path + dest_path)
