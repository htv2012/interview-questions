"""
https://leetcode.com/problems/design-linked-list/description/
"""

import pytest

from solution import MyLinkedList


@pytest.mark.parametrize(
    "actions,args_list,expected_list",
    [
        pytest.param(
            [
                "MyLinkedList",
                "addAtHead",
                "addAtTail",
                "addAtIndex",
                "get",
                "deleteAtIndex",
                "get",
            ],
            [[], [1], [3], [1, 2], [1], [1], [1]],
            [None, None, None, None, 2, None, 3],
            id="Example 1",
        ),
        pytest.param(
            [
                "MyLinkedList",
                "addAtHead",
                "addAtHead",
                "addAtHead",
                "addAtIndex",
                "deleteAtIndex",
                "addAtHead",
                "addAtTail",
                "get",
                "addAtHead",
                "addAtIndex",
                "addAtHead",
            ][[], [7], [2], [1], [3, 0], [2], [6], [4], [4], [4], [5, 0], [6]],
            [None, None, None, None, None, None, None, None, 4, None, None, None],
            id="wrong 1",
        ),
    ],
)
def test_solution(actions, args_list, expected_list):
    li = MyLinkedList()
    for action, args, expected in zip(actions, args_list, expected_list):
        if action == "MyLinkedList":
            li = MyLinkedList()
            continue
        func = getattr(li, action)
        actual = func(*args)
        assert actual == expected, f"{action}({','.join(str(x) for x in args)})"
