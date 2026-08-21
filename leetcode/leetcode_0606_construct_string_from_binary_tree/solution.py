import io

from tree import TreeNode


def tree2str(root: TreeNode | None, buffer: io.StringIO):
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
    def tree2str(self, root: TreeNode | None) -> str:
        buffer = io.StringIO()
        tree2str(root, buffer)
        return buffer.getvalue()
