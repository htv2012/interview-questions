"""
https://leetcode.com/problems/design-a-text-editor/
"""

import itertools

import pytest

from solution import TextEditor


def tc(**kwargs):
    test_id = kwargs.pop("test_id")
    return pytest.param(
        kwargs["actions"],
        kwargs["args_list"],
        kwargs["expected_return"],
        id=test_id,
    )


@pytest.mark.parametrize(
    "actions, args_list, expected_return",
    [
        tc(
            test_id="Example 1",
            actions=[
                "TextEditor",
                "addText",
                "deleteText",
                "addText",
                "cursorRight",
                "cursorLeft",
                "deleteText",
                "cursorLeft",
                "cursorRight",
            ],
            args_list=[[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]],
            expected_return=[
                None,
                None,
                4,
                None,
                "etpractice",
                "leet",
                4,
                "",
                "practi",
            ],
        ),
        tc(
            test_id="Move left too many chars",
            actions=["TextEditor", "addText", "cursorLeft"],
            args_list=[[], ["leetcode"], [40]],
            expected_return=[None, None, ""],
        ),
    ],
)
def test_solution(actions, args_list, expected_return):
    editor = TextEditor()

    for i, action, args, expected in zip(
        itertools.count(), actions, args_list, expected_return
    ):
        if action == "TextEditor":
            continue

        method = getattr(editor, action)
        actual = method(*args)
        assert actual == expected, f"[{i}] {action}({', '.join(repr(x) for x in args)})"
