"""
https://leetcode.com/problems/invert-binary-tree
"""

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.invertTree


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
            root=[4, 2, 7, 1, 3, 6, 9],
            expected=[4, 7, 2, 9, 6, 3, 1],
        ),
        tc(
            test_id="Example 2",
            root=[2, 1, 3],
            expected=[2, 3, 1],
        ),
        tc(
            test_id="Example 3",
            root=[],
            expected=[],
        ),
    ],
)
def test_solution(fut, root, expected):
    #    assert fut(root) == expected
    pass
