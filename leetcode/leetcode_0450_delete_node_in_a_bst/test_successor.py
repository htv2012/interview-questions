"""
https://leetcode.com/problems/delete-node-in-a-bst/
"""

import tree

from common import parametrize
from solution import get_inorder_successor


@parametrize("successor.yaml", ["root", "expected"])
def test_successor(root, expected):
    root_tree = tree.breadth_first_build(root)
    expected_tree = tree.breadth_first_build(expected[0])
    expected_parent = tree.breadth_first_build(expected[1])
    actual_tree, actual_parent = get_inorder_successor(root_tree)
    assert tree.compare_trees(actual_tree, expected_tree)
    assert tree.compare_trees(actual_parent, expected_parent)
