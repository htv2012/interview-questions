import collections
import logging

import pytest

from solution import MinStack

Step = collections.namedtuple("Step", ["action", "args", "expected"])
Entry = collections.namedtuple("E", ["val", "min"])


@pytest.mark.parametrize(
    "steps",
    [
        pytest.param(
            [
                Step(action="MinStack", args=[], expected=None),
                Step(action="push", args=[-2], expected=None),
                Step(action="push", args=[0], expected=None),
                Step(action="push", args=[-3], expected=None),
                Step(action="getMin", args=[], expected=-3),
                Step(action="pop", args=[], expected=None),
                Step(action="top", args=[], expected=0),
                Step(action="getMin", args=[], expected=-2),
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
        logging.debug("Step [%d] %s(%s)", index, action, args_str)
        logging.debug("expected=%r", expected)

        if action == "MinStack":
            obj = MinStack(*args)
        else:
            method = getattr(obj, action)
            assert method is not None
            actual = method(*args)
            logging.debug("actual  =%r", expected)
            assert actual == expected

        logging.debug("obj: %r", obj)
