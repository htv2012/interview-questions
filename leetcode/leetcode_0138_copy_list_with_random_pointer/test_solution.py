"""
https://leetcode.com/problems/copy-list-with-random-pointer/
"""

import pytest

import node
from solution import Solution


@pytest.fixture
def fut():
    sol = Solution()
    return sol.copyRandomList


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["head"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "head, expected",
    [
        tc(
            test_id="Example 1",
            head=[[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
            expected=[[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        ),
        tc(
            test_id="Example 2",
            head=[[1, 1], [2, 1]],
            expected=[[1, 1], [2, 1]],
        ),
        tc(
            test_id="Example 3",
            head=[[3, None], [3, 0], [3, None]],
            expected=[[3, None], [3, 0], [3, None]],
        ),
    ],
)
def test_solution(fut, head, expected):
    input_list = node.build(head)
    expected_list = node.build(head)
    actual_list = fut(input_list)
    node.verify_lists_equal(actual_list, expected_list)
