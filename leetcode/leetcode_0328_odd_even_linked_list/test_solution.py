"""
https://leetcode.com/problems/odd-even-linked-list/
"""

import list_node
import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.oddEvenList


@pytest.mark.parametrize(
    "head,expected",
    [
        pytest.param(
            [1, 2, 3, 4, 5],
            [1, 3, 5, 2, 4],
            id="Example 1",
        ),
        pytest.param(
            [2, 1, 3, 5, 6, 4, 7],
            [2, 3, 6, 7, 1, 5, 4],
            id="Example 2",
        ),
        pytest.param([], [], id="empty list"),
        pytest.param([1], [1], id="list of 1"),
        pytest.param([1, 2], [1, 2], id="list of 2"),
        pytest.param([1, 2, 3], [1, 3, 2], id="list of 3"),
        pytest.param([1, 2, 3, 4], [1, 3, 2, 4], id="list of 4"),
    ],
)
def test_solution(fut, head, expected):
    li = list_node.ListNode.from_iterable(head)
    list_node.assert_values(li, head)
    actual = fut(li)
    list_node.assert_values(actual, expected)
