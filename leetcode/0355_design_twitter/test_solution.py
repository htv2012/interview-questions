import collections
import logging

import pytest

from solution import Twitter

Step = collections.namedtuple("Step", ["action", "args", "expected"])


@pytest.mark.parametrize(
    "steps",
    [
        pytest.param(
            [
                Step(action="Twitter", args=[], expected=None),
                Step(action="postTweet", args=[1, 5], expected=None),
                Step(action="getNewsFeed", args=[1], expected=[5]),
                Step(action="follow", args=[1, 2], expected=None),
                Step(action="postTweet", args=[2, 6], expected=None),
                Step(action="getNewsFeed", args=[1], expected=[6, 5]),
                Step(action="unfollow", args=[1, 2], expected=None),
                Step(action="getNewsFeed", args=[1], expected=[5]),
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
            "Step [%d]: %s(%s), expected: %r", index, action, args_str, expected
        )

        if action == "Twitter":
            obj = Twitter(*args)
        else:
            method = getattr(obj, action)
            assert method is not None
            actual = method(*args)
            assert actual == expected

        # logging.debug("obj=%r", obj)
