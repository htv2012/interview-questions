import logging

import pytest
from list_node import ListNode, assert_values

logger = logging.getLogger()


@pytest.mark.parametrize(
    "head, expected",
    [
        pytest.param([1, 1, 2], [1, 2], id="example 1"),
        pytest.param([1, 1, 2, 3, 3], [1, 2, 3], id="example 2"),
    ],
)
def test_solution(fut, head, expected):
    head = ListNode.from_iterable(head)
    logger.debug("head=%r", head)
    actual = fut(head)
    logger.debug("actual=%r", actual)
    logger.debug("expected=%r", expected)
    assert_values(actual, expected)
