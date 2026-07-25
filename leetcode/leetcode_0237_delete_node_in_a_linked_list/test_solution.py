"""
https://leetcode.com/problems/delete-node-in-a-linked-list/
"""

import list_node
import pytest

from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.deleteNode


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["head_list"],
        kwargs["node_val"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "head_list, node_val, expected",
    [
        tc(
            test_id="Example 1",
            head_list=[4, 5, 1, 9],
            node_val=5,
            expected=[4, 1, 9],
        ),
        tc(
            test_id="Example 2",
            head_list=[4, 5, 1, 9],
            node_val=1,
            expected=[4, 5, 9],
        ),
    ],
)
def test_solution(fut, head_list, node_val, expected):
    head = list_node.build(head_list)
    for node in list_node.iter_list(head):
        if node.val == node_val:
            break
    else:
        raise ValueError(f"cannot find {node_val}")

    fut(node)
    assert list_node.verify_values(head, expected)
