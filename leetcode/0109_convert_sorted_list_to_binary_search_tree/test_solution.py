#!/usr/bin/env python3
import list_node
import pytest
import tree


def same_tree(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False

    if root1.val != root2.val:
        return False
    return same_tree(root1.left, root2.left) and same_tree(root1.right, root2.right)


@pytest.mark.parametrize(
    "head, expected",
    [
        pytest.param([-10, -3, 0, 5, 9], [0, -3, 9, -10, None, 5], id="example 1"),
        pytest.param([], [], id="example 2"),
        pytest.param([1, 2, 3], [2, 1, 3], id="custom 1"),
    ],
)
def test_solution(fut, head, expected):
    head = list_node.ListNode.from_iterable(head)
    expected = tree.breadth_first_build(expected)
    actual = fut(head)
    assert same_tree(actual, expected)
