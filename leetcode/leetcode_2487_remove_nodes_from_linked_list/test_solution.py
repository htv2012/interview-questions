"""
https://leetcode.com/problems/remove-nodes-from-linked-list/
"""

import list_node
import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.removeNodes


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["values"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "values, expected",
    [
        tc(
            test_id="Example 1",
            values=[5, 2, 13, 3, 8],
            expected=[13, 8],
        ),
        tc(
            test_id="Example 2",
            values=[1, 1, 1, 1],
            expected=[1, 1, 1, 1],
        ),
    ],
)
def test_solution(fut, values, expected):
    head = list_node.build(values)
    actual = fut(head)
    assert list_node.verify_values(actual, expected)
