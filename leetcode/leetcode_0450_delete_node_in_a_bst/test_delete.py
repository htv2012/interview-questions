"""
https://leetcode.com/problems/delete-node-in-a-bst/
"""

import logging

import tree

from solution import Solution
from testlib import log_tree, parametrize

logger = logging.getLogger()


@parametrize("delete.yaml", ["root", "key", "expected"])
def test_delete(root, key, expected):
    sol = Solution()
    root_tree = tree.breadth_first_build(root)
    expected_tree = tree.breadth_first_build(expected)

    logger.debug(f"{key = }")
    log_tree(root_tree, "Root Tree")
    log_tree(expected_tree, "Expected Tree")

    actual_tree = sol.deleteNode(root_tree, key)
    log_tree(actual_tree, "Actual Tree")

    assert tree.compare_trees(actual_tree, expected_tree)
