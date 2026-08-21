import list_node
import pytest


def create_lists(list_a: list, list_b: list, skip_a: int, skip_b: int):
    head_a = list_node.ListNode.from_iterable(list_a)

    intersection = head_a
    for _ in range(skip_a):
        intersection = intersection.next

    dummy = list_node.ListNode()
    tail = dummy
    for value in list_b[:skip_b]:
        tail.next = list_node.ListNode(value)
        tail = tail.next
    tail.next = intersection

    return head_a, dummy.next, intersection


@pytest.mark.parametrize(
    "intersect_val, list_a, list_b, skip_a, skip_b",
    [
        pytest.param(8, [4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3, id="example 1"),
        pytest.param(2, [1, 9, 1, 2, 4], [3, 2, 4], 3, 1, id="example 2"),
        pytest.param(0, [2, 6, 4], [1, 5], 3, 2, id="example 3"),
    ],
)
def test_solution(fut, intersect_val, list_a, list_b, skip_a, skip_b):
    head_a, head_b, intersection = create_lists(list_a, list_b, skip_a, skip_b)
    assert fut(head_a, head_b) is intersection
    if intersect_val == 0:
        assert intersection is None
    else:
        assert intersection.val == intersect_val
