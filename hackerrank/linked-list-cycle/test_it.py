import pytest

from main import has_cycle


class SinglyLinkedListNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


def build(seq: list):
    nodes = {}
    pre_head = SinglyLinkedListNode(-1)
    tail = pre_head

    for value in seq:
        if value not in nodes:
            node = SinglyLinkedListNode(value)
            tail.next = node
            tail = node
            nodes[value] = node
        else:
            # tail points back to one of the existing nodes
            tail.next = nodes[value]

    return pre_head.next


def test_build_no_loop():
    head = build([1, 2, 3])
    assert head.data == 1
    assert head.next.data == 2
    assert head.next.next.data == 3
    assert head.next.next.next == None


def test_build_with_loop():
    head = build([1, 2, 1])
    assert head.data == 1
    assert head.next.data == 2
    assert head.next.next is head


@pytest.mark.parametrize(
    "values, expected",
    [
        pytest.param([1, 2, 3], 0, id="no cycle"),
        pytest.param([1], 0, id="no cycle, single node"),
        pytest.param([], 0, id="no cycle, empty list"),
        pytest.param([1, 2, 3, 1], 1, id="cycle to head"),
        pytest.param([1, 2, 3, 2], 1, id="cycle not to head"),
        pytest.param([1, 2, 3, 3], 1, id="cycle to last node"),
        pytest.param(list(range(1000)) + [5], 1, id="cycle large"),
    ],
)
def test_has_cycle(values, expected):
    head = build(values)
    assert has_cycle(head) == expected
