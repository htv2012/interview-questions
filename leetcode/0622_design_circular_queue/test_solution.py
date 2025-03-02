import logging

import pytest

from solution import MyCircularQueue


@pytest.mark.parametrize(
    "actions, args_list, expected_values",
    [
        pytest.param(
            [
                "MyCircularQueue",
                "enQueue",
                "enQueue",
                "enQueue",
                "enQueue",
                "Rear",
                "isFull",
                "deQueue",
                "enQueue",
                "Rear",
            ],
            [[3], [1], [2], [3], [4], [], [], [], [4], []],
            [None, True, True, True, False, 3, True, True, True, 4],
            id="example 1",
        ),
        pytest.param(
            [
                "MyCircularQueue",
                "enQueue",
                "enQueue",
                "enQueue",
                "enQueue",
                "deQueue",
                "deQueue",
                "isEmpty",
                "isEmpty",
                "Rear",
                "Rear",
                "deQueue",
            ],
            [[8], [3], [9], [5], [0], [], [], [], [], [], [], []],
            [None, True, True, True, True, True, True, False, False, 0, 0, True],
            id="wrong 1",
        ),
    ],
)
def test_solution(actions, args_list, expected_values):
    queue = None
    for index, (action, args, expected) in enumerate(
        zip(actions, args_list, expected_values)
    ):
        if action == "MyCircularQueue":
            queue = MyCircularQueue(*args)
        else:
            method = getattr(queue, action)
            actual = method(*args)
            assert (
                actual == expected
            ), f"[{index}] {action}({', '.join(str(arg) for arg in args)})"
        logging.debug(
            "[%d] %s(%s) => %r",
            index,
            action,
            ", ".join(str(arg) for arg in args),
            queue,
        )


def test_front_rear():
    queue = MyCircularQueue(5)
    assert queue.Front() == -1
    assert queue.Rear() == -1

    assert queue.enQueue(195)
    assert queue.Front() == 195
    assert queue.Rear() == 195

    assert queue.enQueue(295)
    assert queue.Front() == 195
    assert queue.Rear() == 295

    assert queue.enQueue(395)
    assert queue.Front() == 195
    assert queue.Rear() == 395

    assert queue.enQueue(495)
    assert queue.Front() == 195
    assert queue.Rear() == 495

    assert queue.enQueue(595)
    assert queue.Front() == 195
    assert queue.Rear() == 595

    # Over capacity
    assert not queue.enQueue(695)
    assert queue.Front() == 195
    assert queue.Rear() == 595
