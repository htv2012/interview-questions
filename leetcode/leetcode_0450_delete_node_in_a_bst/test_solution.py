"""
https://leetcode.com/problems/delete-node-in-a-bst/
"""

import pytest
import tree

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


@pytest.mark.parametrize(
    "root, key, expected",
    [
        tc(
            test_id="Example 1",
            root=[5, 3, 6, 2, 4, None, 7],
            key=3,
            expected=[5, 4, 6, 2, None, None, 7],
        ),
        tc(
            test_id="Example 2",
            root=[5, 3, 6, 2, 4, None, 7],
            key=0,
            expected=[5, 3, 6, 2, 4, None, 7],
        ),
        tc(
            test_id="Example 3",
            root=[],
            key=0,
            expected=[],
        ),
    ],
)
def test_solution(fut, root, key, expected):
    root_tree = tree.breadth_first_build(root)
    expected_tree = tree.breadth_first_build(expected)
    actual_tree = fut(root_tree, key)
    assert tree.compare_trees(actual_tree, expected_tree)
