"""
https://leetcode.com/problems/design-linked-list/description/
"""

import pytest

from solution import MyLinkedList


@pytest.fixture
def li() -> MyLinkedList:
    return MyLinkedList()


@pytest.fixture
def li10(li) -> MyLinkedList:
    for value in range(0, 100, 10):
        li.addAtTail(value)
    return li


def test_create(li):
    assert li.head is None
    assert li.tail is None


def test_add_head(li: MyLinkedList):
    for value in [1, 2, 3]:
        li.addAtHead(value)
        assert li.head.val == value, f"verify head after add head {value}"
        assert li.tail.val == 1, f"verify tail after add head {value}"


def test_add_tail(li: MyLinkedList):
    values = [1, 2, 3]
    for value in values:
        li.addAtTail(value)
        assert li.head.val == 1, f"verify head after add tail {value}"
        assert li.tail.val == value, f"verify tail after add tail {value}"
        assert li.tail.next is None, f"verify tail.next after add tail {value}"


@pytest.mark.parametrize("index", list(range(5)))
def test_get(li10: MyLinkedList, index):
    assert li10.get(index) == index * 10


@pytest.mark.parametrize("index", [-1, 0, 100])
def test_get_expect_out_of_range(li10: MyLinkedList, index: int):
    with pytest.raises(ValueError):
        li10.get(index)


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
