"""
https://leetcode.com/problems/implement-stack-using-queues/description/
"""

import types

import pytest

from solution import MyStack


@pytest.mark.parametrize(
    "test_case",
    [
        pytest.param(
            types.SimpleNamespace(
                actions=["MyStack", "push", "push", "top", "pop", "empty"],
                args_list=[[], [1], [2], [], [], []],
                expected=[None, None, None, 2, 2, False],
            ),
            id="Example 1",
        ),
    ],
)
def test_solution(test_case):
    stack = MyStack()
    steps = zip(test_case.actions, test_case.args_list, test_case.expected)
    for action, args, expected in steps:
        if action == "MyStack":
            stack = MyStack()
            continue

        func = getattr(stack, action)
        print(f"{stack.data[:10]=}")
        assert func(*args) == expected, f"{action=}, {args=}"
