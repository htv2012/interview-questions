"""
https://leetcode.com/problems/cousins-in-binary-tree-ii/
"""

import logging

import pytest
from tree import breadth_first_build, compare_trees

from solution import Solution

logger = logging.getLogger()


@pytest.fixture
def fut():
    sol = Solution()
    return sol.replaceValueInTree


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["root"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "root, expected",
    [
        tc(
            test_id="Example 1",
            root=[5, 4, 9, 1, 10, None, 7],
            expected=[0, 0, 0, 7, 7, None, 11],
        ),
        tc(
            test_id="Example 2",
            root=[3, 1, 2],
            expected=[0, 0, 0],
        ),
    ],
)
def test_solution(fut, root, expected):
    root = breadth_first_build(root)
    root = fut(root)
    expected = breadth_first_build(expected)
    assert compare_trees(root, expected)
