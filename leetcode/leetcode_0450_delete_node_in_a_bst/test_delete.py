"""
https://leetcode.com/problems/delete-node-in-a-bst/
"""

import pytest
import tree

from common import log_tree, parametrize
from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.deleteNode


@parametrize("delete.yaml", ["root", "key", "expected"])
def test_delete(fut, root, key, expected):
    root_tree = tree.breadth_first_build(root)
    log_tree(root_tree, "Root Tree")

    expected_tree = tree.breadth_first_build(expected)
    log_tree(expected_tree, "Expected Tree")

    actual_tree = fut(root_tree, key)
    log_tree(actual_tree, "Actual Tree")

    assert tree.compare_trees(actual_tree, expected_tree)
