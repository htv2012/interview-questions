import pytest
from list_node import ListNode

from solution import count_nodes


@pytest.mark.parametrize(
    "values, expected",
    [([], 0), ([9], 1), ([10, 10], 2), ([10, 11, 12], 3)],
)
def test_count_nodes(values, expected):
    head = ListNode.from_iterable(values)
    assert count_nodes(head) == expected
