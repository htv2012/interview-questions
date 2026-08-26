"""
https://leetcode.com/problems/insertion-sort-list/
"""

import list_node
import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.insertionSortList


def tc(id, values, expected):
    return pytest.param(values, expected, id=id)


@pytest.mark.parametrize(
    "values, expected",
    [
        tc(id="Example 1", values=[4, 2, 1, 3], expected=[1, 2, 3, 4]),
        tc(id="Example 2", values=[-1, 5, 3, 4, 0], expected=[-1, 0, 3, 4, 5]),
        tc(id="empty", values=[], expected=[]),
        tc(id="single node", values=[5], expected=[5]),
        tc(id="same values", values=[1, 1, 1], expected=[1, 1, 1]),
        tc(
            id="exercise insertion points",
            values=[3, 5, 1, 4, 8],
            expected=[1, 3, 4, 5, 8],
        ),
    ],
)
def test_solution(fut, values, expected):
    head = list_node.build(values)
    actual = fut(head)
    assert list_node.verify_values(actual, expected)
