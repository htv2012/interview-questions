import list_node
import pytest


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param([1, 2, 3, 4], [1, 4, 2, 3], id="example 1"),
        pytest.param([1, 2, 3, 4, 5], [1, 5, 2, 4, 3], id="example 2"),
    ],
)
def test_solution(fut, indata, expected):
    head = list_node.ListNode.from_iterable(indata)
    fut(head)
    actual = [node.val for node in list_node.iter_list(head)]
    assert actual == expected
