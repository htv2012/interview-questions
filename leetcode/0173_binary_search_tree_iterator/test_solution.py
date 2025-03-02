#!/usr/bin/env python3
import pytest
import tree

from solution import BSTIterator


@pytest.mark.parametrize(
    "root, actions, expected",
    [
        pytest.param(
            [7, 3, 15, None, None, 9, 20],
            [
                "BSTIterator",
                "next",
                "next",
                "hasNext",
                "next",
                "hasNext",
                "next",
                "hasNext",
                "next",
                "hasNext",
            ],
            [None, 3, 7, True, 9, True, 15, True, 20, False],
            id="example 1",
        ),
        pytest.param(
            [4, 2, 6, 1, 3, 5, 7],
            [
                "hasNext",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "hasNext",
            ],
            [True, 1, 2, 3, 4, 5, 6, 7, False],
            id="custom 1",
        ),
    ],
)
def test_solution(root, actions, expected):
    root = tree.breadth_first_build(root)
    actual = []
    bsti = BSTIterator(root)

    for action in actions:
        if action == "BSTIterator":
            actual.append(None)
            continue

        method = getattr(bsti, action)
        actual.append(method())

    assert actual == expected
