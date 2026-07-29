import list_node
import pytest

from main import removeDuplicates


@pytest.mark.parametrize(
    "values, expected",
    [
        pytest.param([1, 1, 2, 2, 2, 3, 3, 3], [1, 2, 3], id="happy path"),
        pytest.param([], [], id="empty"),
        pytest.param([1], [1], id="single node"),
        pytest.param([1] * 1000, [1], id="all of same value"),
    ],
)
def test_remove_duplicates(values, expected):
    head = list_node.build(values)
    actual = removeDuplicates(head)
    assert list_node.verify_values(actual, expected)
