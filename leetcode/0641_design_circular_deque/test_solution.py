import collections
import logging

import pytest

from solution import MyCircularDeque

Step = collections.namedtuple("Step", ["action", "args", "expected"])


@pytest.mark.parametrize(
    "steps",
    [
        pytest.param(
            [
                Step(action="MyCircularDeque", args=[3], expected=None),
                Step(action="insertLast", args=[1], expected=True),
                Step(action="insertLast", args=[2], expected=True),
                Step(action="insertFront", args=[3], expected=True),
                Step(action="insertFront", args=[4], expected=False),
                Step(action="getRear", args=[], expected=2),
                Step(action="isFull", args=[], expected=True),
            ],
            id="example 1",
        ),
        pytest.param(
            [
                Step(action="MyCircularDeque", args=[5], expected=None),
                Step(action="isEmpty", args=[], expected=True),
                Step(action="isFull", args=[], expected=False),
                Step(action="insertLast", args=[100], expected=True),
                Step(action="getRear", args=[], expected=100),
                Step(action="getFront", args=[], expected=100),
                Step(action="deleteFront", args=[], expected=True),
                Step(action="deleteFront", args=[], expected=False),
                Step(action="deleteLast", args=[], expected=False),
            ],
            id="my 1",
        ),
        pytest.param(
            [
                Step(action="MyCircularDeque", args=[3], expected=None),
                Step(action="insertFront", args=[2], expected=True),
                Step(action="insertLast", args=[4], expected=True),
                Step(action="insertFront", args=[6], expected=True),
                Step(action="getRear", args=[], expected=4),
            ],
            id="wrong 1",
        ),
    ],
)
def test_solution(steps):
    queue = None
    for index, step in enumerate(steps):
        logging.debug(
            "================================================================================"
        )
        logging.debug("Step %r", step)

        if step.action == "MyCircularDeque":
            logging.debug("[%d] MyCircularDeque(%d)", index, step.args[0])
            queue = MyCircularDeque(*step.args)
        else:
            method = getattr(queue, step.action)
            assert method is not None
            actual = method(*step.args)

            args_str = ", ".join(str(x) for x in step.args)
            msg = "[%d] %s(%s)" % (index, step.action, args_str)
            logging.debug("[%d] %s(%s) => %r", index, step.action, args_str, actual)

            assert actual == step.expected, msg

        logging.debug("Queue: %r", queue)


def test_empty():
    queue = MyCircularDeque(3)
    assert queue.isEmpty()
