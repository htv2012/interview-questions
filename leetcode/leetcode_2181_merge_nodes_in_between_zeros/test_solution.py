"""
https://leetcode.com/problems/merge-nodes-in-between-zeros/
"""

import list_node
import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.mergeNodes


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["node_values"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "node_values, expected",
    [
        tc(test_id="Example 1", node_values=[0, 3, 1, 0, 4, 5, 2, 0], expected=[4, 11]),
        tc(
            test_id="Example 2",
            node_values=[0, 1, 0, 3, 0, 2, 2, 0],
            expected=[1, 3, 4],
        ),
        tc(test_id="one segment", node_values=[0, 5, 0], expected=[5]),
    ],
)
def test_solution(fut, node_values, expected):
    head = list_node.build(node_values)
    actual = fut(head)
    assert list_node.verify_values(actual, expected)
