import pytest
from list_node import ListNode


@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        pytest.param([7, 2, 4, 3], [5, 6, 4], [7, 8, 0, 7], id="example 1"),
        pytest.param([2, 4, 3], [5, 6, 4], [8, 0, 7], id="example 2"),
        pytest.param([0], [0], [0], id="example 3"),
    ],
)
def test_solution(fut, list1, list2, expected):
    list1 = ListNode.from_iterable(list1)
    list2 = ListNode.from_iterable(list2)
    node = fut(list1, list2)
    actual = []
    while node is not None:
        actual.append(node.val)
        node = node.next

    assert actual == expected
