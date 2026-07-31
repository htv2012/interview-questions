"""
https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
"""

import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.isValidSerialization


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["preorder"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "preorder, expected",
    [
        tc(
            test_id="Example 1",
            preorder="9,3,4,#,#,1,#,#,2,#,6,#,#",
            expected=True,
        ),
        tc(
            test_id="Example 2",
            preorder="1,#",
            expected=False,
        ),
        tc(
            test_id="Example 3",
            preorder="9,#,#,1",
            expected=False,
        ),
    ],
)
def test_solution(fut, preorder, expected):
    assert fut(preorder) == expected
