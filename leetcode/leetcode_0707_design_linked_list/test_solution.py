"""
https://leetcode.com/problems/design-linked-list/description/
"""

import pytest

from solution import MyLinkedList


@pytest.fixture
def li() -> MyLinkedList:
    return MyLinkedList()


def test_create(li):
    assert li.head is None
    assert li.tail is None


def test_add_head_when_empty(li: MyLinkedList):
    li.addAtHead(9)
    assert li.head is li.tail
    assert li.head.val == 9
    assert li.head.next is None


def test_add_tail(li: MyLinkedList):
    values = [1, 2, 3]
    for value in values:
        li.addAtTail(value)
        assert li.head.val == 1, f"verify head after adding {value}"
        assert li.tail.val == value, f"verify tail after adding {value}"
        assert li.tail.next is None, f"verify tail.next after adding {value}"


@pytest.mark.parametrize(
    "actions,args_list,expected_list",
    [
        pytest.param(
            [
                "MyLinkedList",
                "addAtHead",
                "addAtTail",
                "addAtIndex",
                "get",
                "deleteAtIndex",
                "get",
            ],
            [[], [1], [3], [1, 2], [1], [1], [1]],
            [None, None, None, None, 2, None, 3],
            id="Example 1",
        ),
    ],
)
def test_solution(actions, args_list, expected_list):
    li = MyLinkedList()
    for action, args, expected in zip(actions, args_list, expected_list):
        if action == "MyLinkedList":
            li = MyLinkedList()
            continue
        action = getattr(li, action)
        assert action(*args) == expected
