import pytest
from list_node import ListNode

from solution import get_node_at_position

VALUES = [1, 2, 3, 4, 5]


@pytest.fixture
def head():
    list_head = ListNode.from_iterable(VALUES)
    return list_head


def test_last_position(head):
    node = get_node_at_position(head, 5)
    assert node.val == VALUES[4]


def test_position_1(head):
    node = get_node_at_position(head, 1)
    assert node is head
    assert node.val == VALUES[0]


def test_mid_positions(head):
    left, right = 2, 5
    left_node = get_node_at_position(head, left)
    assert left_node.val == VALUES[left - 1]

    right_node = get_node_at_position(left_node, right - left + 1)
    assert right_node.val == VALUES[right - 1]
