"""
https://leetcode.com/problems/linked-list-cycle-ii/
"""

import contextlib

import pytest
from list_node import ListNode

from solution import Solution


def build_list_with_loop(list_values: list[int], loop_index: int):
    nodes = [ListNode(v) for v in list_values]
    for i, node in enumerate(nodes, 1):
        with contextlib.suppress(IndexError):
            node.next = nodes[i]

    if loop_index != -1:
        nodes[-1].next = nodes[loop_index]

    return nodes[0] if nodes else None


@pytest.mark.parametrize(
    "list_values, pos, expected",
    [
        pytest.param([3, 2, 0, -4], 1, 2, id="Example 1"),
        pytest.param([1, 2], 0, 1, id="Example 2"),
        pytest.param([1], -1, "no cycle", id="Example 3"),
        pytest.param([], -1, "no cycle", id="empty list"),
    ],
)
def test_solution(list_values, pos, expected):
    head = build_list_with_loop(list_values, pos)
    sol = Solution()
    entry = sol.detectCycle(head)
    if pos == -1:
        assert entry is None
    else:
        assert entry.val == expected
