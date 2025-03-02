import collections
import logging

import pytest

from solution import BrowserHistory

Step = collections.namedtuple("Step", ["action", "args", "expected"])


@pytest.mark.parametrize(
    "steps",
    [
        pytest.param(
            [
                Step(action="BrowserHistory", args=["leetcode.com"], expected=None),
                Step(action="visit", args=["google.com"], expected=None),
                Step(action="visit", args=["facebook.com"], expected=None),
                Step(action="visit", args=["youtube.com"], expected=None),
                Step(action="back", args=[1], expected="facebook.com"),
                Step(action="back", args=[1], expected="google.com"),
                Step(action="forward", args=[1], expected="facebook.com"),
                Step(action="visit", args=["linkedin.com"], expected=None),
                Step(action="forward", args=[2], expected="linkedin.com"),
                Step(action="back", args=[2], expected="google.com"),
                Step(action="back", args=[7], expected="leetcode.com"),
            ],
            id="example 1",
        ),
    ],
)
def test_solution(steps):
    obj = None
    for index, (action, args, expected) in enumerate(steps):
        logging.debug("============================================================")
        args_str = ", ".join(str(arg) for arg in args)
        logging.debug(
            "Step [%d] %s(%s), expected=%r", index, action, args_str, expected
        )

        if action == "BrowserHistory":
            obj = BrowserHistory(*args)
        else:
            method = getattr(obj, action)
            assert method is not None
            actual = method(*args)
            assert actual == expected

        logging.debug("obj=%r", obj)
