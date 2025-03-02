from tree import TreeNode


def find(root: "TreeNode", target: "TreeNode", path: tuple = tuple()) -> tuple:
    if root is None:
        return tuple()

    path = path + (root,)
    if root.val == target.val:
        return path
    elif found := find(root.left, target, path):
        return found
    elif found := find(root.right, target, path):
        return found
    else:
        return tuple()


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root is None:
            return None

        p_path = find(root, p)
        q_path = find(root, q)

        last = None
        for p_node, q_node in zip(p_path, q_path):
            if p_node is not q_node:
                break
            last = p_node
        return last
