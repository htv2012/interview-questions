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
        tc(
            test_id="single node, found",
            root=[9],
            key=9,
            expected=[],
        ),
        tc(
            test_id="single node, not found",
            root=[9],
            key=9,
            expected=[9],
        ),
        tc(
            test_id="delete 500, replaced by 550",
            root=[
                1000,
                500,
                2000,
                250,
                750,
                1500,
                2500,
                100,
                300,
                600,
                800,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                550,
                700,
            ],
            key=500,
            expected=[
                1000,
                550,
                2000,
                250,
                750,
                1500,
                2500,
                100,
                300,
                600,
                800,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                700,
            ],
        ),
        tc(
            test_id="leaf node",
            root=[1000, 500],
            key=500,
            expected=[1000],
        ),
        tc(
            test_id="node only right child",
            root=[1000, 500, 2000, None, 750],
            key=500,
            expected=[1000, 750, 2000],
        ),
    ],
)
def test_solution(fut, root, key, expected):
    root_tree = tree.breadth_first_build(root)
    expected_tree = tree.breadth_first_build(expected)
    actual_tree = fut(root_tree, key)
    assert tree.compare_trees(actual_tree, expected_tree)
