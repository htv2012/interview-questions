import list_node
import pytest


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param([1, 8, 9], [3, 7, 8], id="example 1"),
        pytest.param([9, 9, 9], [1, 9, 9, 8], id="example 2"),
        pytest.param([0], [0], id="zero"),
    ],
)
def test_solution(fut, indata, expected):
    head = list_node.ListNode.from_iterable(indata)
    actual = fut(head)
    actual = [node.val for node in list_node.iter_list(actual)]
    assert actual == expected
