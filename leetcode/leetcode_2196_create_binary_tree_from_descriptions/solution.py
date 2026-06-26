from typing import List, Optional

from tree import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # descriptions: [[parent,child,isleft],...]
        nodes = {}  # dict {value: node}
        has_parent = set()  # set of values of those nodes which have parent

        for parent_value, child_value, is_left in descriptions:
            parent_node = nodes.setdefault(parent_value, TreeNode(parent_value))
            child_node = nodes.setdefault(child_value, TreeNode(child_value))
            has_parent.add(child_value)

            if is_left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

        # Find the root
        if len(nodes) == 0:
            return None

        root_set = nodes.keys() - has_parent
        assert len(root_set) == 1, f"Expect 1 root, but found {root_set}"
        root_value = root_set.pop()
        return nodes[root_value]
