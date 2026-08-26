"""
https://leetcode.com/problems/delete-node-in-a-bst/
"""

import tree

from solution import get_inorder_successor
from testlib import parametrize


@parametrize("successor.yaml", ["root", "expected"])
def test_successor(root, expected):
    expected_tree = tree.breadth_first_build(expected[0])
    expected_parent = tree.breadth_first_build(expected[1])
    expected_side = expected[2]

    root_tree = tree.breadth_first_build(root)
    actual_tree, actual_parent, actual_side = get_inorder_successor(root_tree)

    assert tree.compare_trees(actual_tree, expected_tree)
    assert tree.compare_trees(actual_parent, expected_parent)
    assert actual_side == expected_side
