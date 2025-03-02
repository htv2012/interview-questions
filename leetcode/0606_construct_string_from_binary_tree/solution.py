import io
from typing import Optional

from common.tree import TreeNode


def tree2str(root: Optional[TreeNode], buffer: io.StringIO):
    if root is None:
        return

    buffer.write(str(root.val))
    if root.left is None and root.right is None:
        return

    buffer.write("(")
    tree2str(root.left, buffer)
    buffer.write(")")

    if root.right is None:
        return
    buffer.write("(")
    tree2str(root.right, buffer)
    buffer.write(")")


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        buffer = io.StringIO()
        tree2str(root, buffer)
        return buffer.getvalue()
