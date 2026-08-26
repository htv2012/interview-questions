import collections
import logging

import pytest

from solution import AuthenticationManager

logger = logging.getLogger()

Step = collections.namedtuple("Step", ["action", "args", "expected"])


@pytest.mark.parametrize(
    "steps",
    [
        pytest.param(
            [
                Step(action="AuthenticationManager", args=[5], expected=None),
                Step(action="renew", args=["aaa", 1], expected=None),
                Step(action="generate", args=["aaa", 2], expected=None),
                Step(action="countUnexpiredTokens", args=[6], expected=1),
                Step(action="generate", args=["bbb", 7], expected=None),
                Step(action="renew", args=["aaa", 8], expected=None),
                Step(action="renew", args=["bbb", 10], expected=None),
                Step(action="countUnexpiredTokens", args=[15], expected=0),
            ],
            id="example 1",
        ),
    ],
)
def test_solution(steps):
    obj = None
    for index, (action, args, expected) in enumerate(steps):
        logger.debug("============================================================")
        args_str = ", ".join(repr(arg) for arg in args)
        logger.debug("Step [%d] %s(%s)", index, action, args_str)

        if action == "AuthenticationManager":
            obj = AuthenticationManager(*args)
        else:
            logger.debug("expected=%r", expected)
            method = getattr(obj, action)
            assert method is not None
            actual = method(*args)
            logger.debug("actual=%r", actual)
            assert actual == expected
