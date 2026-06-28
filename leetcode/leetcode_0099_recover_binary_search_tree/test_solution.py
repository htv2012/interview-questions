"""
https://leetcode.com/problems/recover-binary-search-tree/
"""

import pytest
from tree import breadth_first_build, verify_binary_search_tree

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.recoverTree


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
            root=[1, 3, None, None, 2],
            expected=[3, 1, None, None, 2],
        ),
        tc(
            test_id="Example 2",
            root=[3, 1, 4, None, None, 2],
            expected=[2, 1, 4, None, None, 3],
        ),
    ],
)
def test_solution(fut, root, expected):
    root = breadth_first_build(root)
    fut(root)
    assert verify_binary_search_tree(root)
