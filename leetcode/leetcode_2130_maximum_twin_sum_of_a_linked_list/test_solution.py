import list_node
import pytest


@pytest.mark.parametrize(
    "indata, expected",
    [
        pytest.param([5, 4, 2, 1], 6, id="example 1"),
        pytest.param([4, 2, 2, 3], 7, id="example 2"),
        pytest.param([1, 100000], 100001, id="example 3"),
    ],
)
def test_solution(fut, indata, expected):
    head = list_node.ListNode.from_iterable(indata)
    assert fut(head) == expected
