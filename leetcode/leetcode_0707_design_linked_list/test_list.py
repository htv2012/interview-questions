"""
https://leetcode.com/problems/design-linked-list/description/
"""

import pytest

from solution import MyLinkedList


@pytest.fixture
def li() -> MyLinkedList:
    """Empty list."""
    return MyLinkedList()


LIST_CONTENT = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]


@pytest.fixture
def li10(li) -> MyLinkedList:
    """List with 10 elements."""
    for value in LIST_CONTENT:
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


@pytest.mark.parametrize("index", [-5, 1, 100])
def test_get_expect_out_of_range(li10: MyLinkedList, index: int):
    li10.get(index) == -1


def test_add_at_index_scenario(li: MyLinkedList):
    # add at index 0 is the same as add at head
    for value in [2, 1, 0]:
        li.addAtIndex(0, value)
        assert li.head.val == value, f"verify add at index 0, {value=}"
    assert [node.val for node in li] == [0, 1, 2]

    # add at index == len will append
    for index, value in zip([3, 4, 5], [300, 400, 500]):
        li.addAtIndex(index, value)
    assert [node.val for node in li] == [0, 1, 2, 300, 400, 500]

    # add at index 1
    for value in [10, 20, 30]:
        li.addAtIndex(1, value)
    assert [node.val for node in li] == [0, 30, 20, 10, 1, 2, 300, 400, 500]


@pytest.mark.parametrize(
    "index, value, expected, expected_tail",
    [
        pytest.param(0, 999, [999] + LIST_CONTENT, 90, id="add at index 0"),
        pytest.param(10, 999, LIST_CONTENT + [999], 999, id="add at last"),
        pytest.param(1, 999, [0, 999] + LIST_CONTENT[1:], 90, id="add at index 1"),
        pytest.param(
            9, 999, LIST_CONTENT[:-1] + [999, 90], 90, id="add at next-to-last"
        ),
        pytest.param(-1, 999, LIST_CONTENT, 90, id="add at index -1"),
        pytest.param(11, 999, LIST_CONTENT, 90, id="add pass the length"),
        pytest.param(100, 999, LIST_CONTENT, 90, id="add way pass the length"),
    ],
)
def test_add_at_index(
    li10: MyLinkedList, index: int, value: int, expected: list, expected_tail: int
):
    li10.addAtIndex(index, value)
    assert [node.val for node in li10] == expected
    assert li10.tail.val == expected_tail


@pytest.mark.parametrize(
    "index,expected",
    [
        pytest.param(0, LIST_CONTENT[1:], id="delete at head"),
        pytest.param(1, [0] + LIST_CONTENT[2:], id="delete at head + 1"),
        pytest.param(8, LIST_CONTENT[:8] + [90], id="delete at tail - 1"),
        pytest.param(9, LIST_CONTENT[:9], id="delete at tail"),
        pytest.param(10, LIST_CONTENT, id="delete 1 pass tail"),
        pytest.param(-1, LIST_CONTENT, id="delete beyond list head"),
        pytest.param(11, LIST_CONTENT, id="delete beyond list tail"),
        pytest.param(5, LIST_CONTENT[:5] + LIST_CONTENT[6:], id="delete at middle"),
    ],
)
def test_delete(li10: MyLinkedList, index, expected):
    li10.deleteAtIndex(index)
    assert [node.val for node in li10] == expected
