#!/usr/bin/env python3
import pytest

from solution import Trie


@pytest.mark.parametrize(
    "actions, args_list, expected_list",
    [
        pytest.param(
            ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
            [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
            [None, None, True, False, True, None, True],
            id="example 1",
        ),
    ],
)
def test_solution(actions, args_list, expected_list):
    obj = None
    for action, args, expected in zip(actions, args_list, expected_list):
        if action == "Trie":
            obj = Trie(*args)
            actual = None
        else:
            method = getattr(obj, action)
            actual = method(*args)
        assert actual is expected, f"{action=}, {args=}"
