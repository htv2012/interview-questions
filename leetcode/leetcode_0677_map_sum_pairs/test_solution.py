"""
https://leetcode.com/problems/map-sum-pairs/
"""

import pytest

from solution import MapSum


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
            actions=["MapSum", "insert", "sum", "insert", "sum"],
            args_list=[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]],
            expected=[None, None, 3, None, 5],
        ),
    ],
)
def test_solution(actions, args_list, expected):
    ms = MapSum()
    for action, args, expected_value in zip(actions, args_list, expected):
        if action == "MapSum":
            continue

        method = getattr(ms, action)
        actual = method(*args)
        assert actual == expected_value
