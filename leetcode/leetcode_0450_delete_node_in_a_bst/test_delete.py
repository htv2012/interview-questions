"""
https://leetcode.com/problems/delete-node-in-a-bst/
"""

import pytest
import tree

from common import parametrize
from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.deleteNode


@parametrize("delete.yaml", ["root", "key", "expected"])
def test_delete(fut, root, key, expected):
    root_tree = tree.breadth_first_build(root)
    expected_tree = tree.breadth_first_build(expected)
    actual_tree = fut(root_tree, key)
    assert tree.compare_trees(actual_tree, expected_tree)
