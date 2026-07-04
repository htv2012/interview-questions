"""
https://leetcode.com/problems/delete-node-in-a-bst/
"""

import pytest
import tree
import yaml

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.deleteNode


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["root"],
        kwargs["key"],
        kwargs["expected"],
        id=test_id,
    )


def get_test_cases():
    with open("delete.yaml") as stream:
        test_cases = yaml.safe_load(stream)

    return [tc(**test_case) for test_case in test_cases]


@pytest.mark.parametrize("root, key, expected", get_test_cases())
def test_delete(fut, root, key, expected):
    root_tree = tree.breadth_first_build(root)
    expected_tree = tree.breadth_first_build(expected)
    actual_tree = fut(root_tree, key)
    assert tree.compare_trees(actual_tree, expected_tree)
