"""
https://leetcode.com/problems/implement-router/
"""

import types

import pytest

from solution import Router


@pytest.mark.parametrize(
    "test_case",
    [
        pytest.param(
            types.SimpleNamespace(
                actions=[
                    "Router",
                    "addPacket",
                    "addPacket",
                    "addPacket",
                    "addPacket",
                    "addPacket",
                    "forwardPacket",
                    "addPacket",
                    "getCount",
                ],
                args_list=[
                    [3],
                    [1, 4, 90],
                    [2, 5, 90],
                    [1, 4, 90],
                    [3, 5, 95],
                    [4, 5, 105],
                    [],
                    [5, 2, 110],
                    [5, 100, 110],
                ],
                expected=[None, True, True, False, True, True, [2, 5, 90], True, 1],
            ),
            id="Example 1",
        ),
        pytest.param(
            types.SimpleNamespace(
                actions=["Router", "addPacket", "forwardPacket", "forwardPacket"],
                args_list=[[2], [7, 4, 90], [], []],
                expected=[None, True, [7, 4, 90], []],
            ),
            id="Example 2",
        ),
        pytest.param(
            types.SimpleNamespace(
                actions=["Router", "addPacket", "getCount"],
                args_list=[[3], [1, 4, 90], [5, 100, 110]],
                expected=[None, True, 0],
            ),
            id="key error",
        ),
    ],
)
def test_solution(test_case):
    combo = zip(test_case.actions, test_case.args_list, test_case.expected)
    for action, args, expected in combo:
        if action == "Router":
            router = Router(*args)
            assert expected is None
        else:
            func = getattr(router, action)
            actual = func(*args)
            assert actual == expected
