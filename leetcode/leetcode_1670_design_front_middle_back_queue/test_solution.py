"""
https://leetcode.com/problems/design-front-middle-back-queue/
"""

import pytest

from solution import FrontMiddleBackQueue


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["actions"],
        kwargs["args_list"],
        kwargs["expected"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "actions, args_list, expected",
    [
        tc(
            test_id="Example 1",
            actions=[
                "FrontMiddleBackQueue",
                "pushFront",
                "pushBack",
                "pushMiddle",
                "pushMiddle",
                "popFront",
                "popMiddle",
                "popMiddle",
                "popBack",
                "popFront",
            ],
            args_list=[[], [1], [2], [3], [4], [], [], [], [], []],
            expected=[None, None, None, None, None, 1, 3, 4, 2, -1],
        ),
    ],
)
def test_solution(actions, args_list, expected):
    que = FrontMiddleBackQueue()
    for action, args, expected_value in zip(actions, args_list, expected):
        if action == "FrontMiddleBackQueue":
            que = FrontMiddleBackQueue(*args)
            continue
        method = getattr(que, action)
        actual = method(*args)
        assert actual == expected_value
