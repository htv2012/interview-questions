"""
https://leetcode.com/problems/cousins-in-binary-tree/
"""

import pytest
import tree

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.isCousins


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["root"],
        kwargs["x"],
        kwargs["y"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "root, x, y, expected",
    [
        tc(
            test_id="Example 1",
            root=[1, 2, 3, 4],
            x=4,
            y=3,
            expected=False,
        ),
        tc(
            test_id="Example 2",
            root=[1, 2, 3, None, 4, None, 5],
            x=5,
            y=4,
            expected=True,
        ),
        tc(
            test_id="Example 3",
            root=[1, 2, 3, None, 4],
            x=2,
            y=3,
            expected=False,
        ),
    ],
)
def test_solution(fut, root, x, y, expected):
    root = tree.breadth_first_build(root)
    assert fut(root, x, y) == expected
