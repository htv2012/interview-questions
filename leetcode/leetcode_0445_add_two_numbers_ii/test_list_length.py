import pytest
from list_node import ListNode

from solution import list_length


@pytest.mark.parametrize(
    ["head", "expected"],
    [
        pytest.param([], 0, id="empty"),
        pytest.param([5], 1, id="single node"),
        pytest.param([1, 2], 2, id="two item"),
        pytest.param([1, 2, 3], 3, id="three item"),
    ],
)
def test_length(head, expected):
    head = ListNode.from_iterable(head)
    assert list_length(head) == expected
