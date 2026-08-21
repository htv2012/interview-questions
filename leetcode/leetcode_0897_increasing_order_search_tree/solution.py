from tree import TreeNode


def inorder_iter(root):
    if root is None:
        return
    yield from inorder_iter(root.left)
    yield root
    yield from inorder_iter(root.right)


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        node = pre_root = TreeNode(val=None)
        for original_node in inorder_iter(root):
            node.right = original_node
            node = original_node
            node.left = None

        return pre_root.right
